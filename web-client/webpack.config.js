const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const path = require('path');
var __dirname;
const srcDir = path.resolve(__dirname, 'src');
const distDir = path.resolve(__dirname, '..', 'public');

const urlLoader = {
    loader: 'url-loader',
    options: {
        limit: 8192
    }
};

const config = {
    entry: {
        index: srcDir + '/index.js'
    },
    output: {
        path: distDir,
        filename: '[name]-[hash].js'
    },
    module: {
        rules: [
            {
                oneOf: [
                    {
                        test: /\.css$/,
                        use: ['style-loader', 'css-loader']
                    },
                    {
                        test: /\.(js|jsx|mjs)$/,
                        exclude: /(node_modules|bower_components)/,
                        use: 'babel-loader'
                    },
                    {
                        test: /\.(eot|woff|woff2?|ttf|png|jpe?g|gif|svg)(\?.*)?$/,
                        use: urlLoader
                    },
                    {
                        exclude: [/\.(js|jsx|mjs)$/, /\.html$/, /\.json$/],
                        use: 'file-loader'
                    },
                ]
            }
        ]
    },
    mode: 'development',
    devtool: '#eval-source-map',
    plugins: [
        new HtmlWebpackPlugin({
            favicon: './src/favicon.png',
            template: './src/index.html',
            filename: 'index.html',
            title: 'Top News'
        })
    ]
};

if (process.env.NODE_ENV === 'production') {
    config.mode = 'production';
    config.devtool = '#source-map';
    config.plugins = (config.plugins || []).concat([
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: '"production"'
            }
        }),
        new webpack.optimize.UglifyJsPlugin({
            sourceMap: true,
            compress: {
                warnings: false
            }
        }),
        new webpack.LoaderOptionsPlugin({
            minimize: true
        })
    ]);
}

module.exports = config;