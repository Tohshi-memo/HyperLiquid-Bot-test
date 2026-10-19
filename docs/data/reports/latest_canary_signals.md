# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T04:37:27.556816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `13`; crypto_alt avg `0.0157` n `237`; crypto_major avg `0.0436` n `8`; equity avg `0.0155` n `151`; fx avg `0.0102` n `6`; index avg `-0.0014` n `26`; metal avg `0.0201` n `20`; unknown avg `2.5499` n `1194`
- 1h: commodity avg `0.0356` n `13`; crypto_alt avg `-0.2296` n `237`; crypto_major avg `-0.0195` n `8`; equity avg `-0.0747` n `151`; fx avg `0.005` n `6`; index avg `-0.0112` n `26`; metal avg `-0.0059` n `20`; unknown avg `3.0183` n `1186`
- 4h: commodity avg `-0.0315` n `13`; crypto_alt avg `0.2656` n `237`; crypto_major avg `0.5648` n `8`; equity avg `1.221` n `151`; fx avg `-0.0243` n `6`; index avg `0.2188` n `26`; metal avg `0.1406` n `20`; unknown avg `0.4424` n `1150`
- 24h: commodity avg `-0.4497` n `13`; crypto_alt avg `-0.3579` n `237`; crypto_major avg `0.7129` n `8`; equity avg `2.7231` n `151`; fx avg `0.0049` n `6`; index avg `0.5029` n `26`; metal avg `0.3177` n `20`; unknown avg `3.1097` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1972`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1433`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1196`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0984`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0739`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0727`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0647`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
