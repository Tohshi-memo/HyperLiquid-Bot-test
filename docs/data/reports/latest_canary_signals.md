# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T19:52:27.472426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `13`; crypto_alt avg `0.0028` n `239`; crypto_major avg `-0.0233` n `8`; equity avg `-0.0541` n `161`; fx avg `-0.0076` n `6`; index avg `-0.005` n `27`; metal avg `-0.0231` n `20`; unknown avg `1.3064` n `1262`
- 1h: commodity avg `-0.2741` n `13`; crypto_alt avg `-0.1908` n `239`; crypto_major avg `-0.2208` n `8`; equity avg `-0.6429` n `161`; fx avg `0.0135` n `6`; index avg `-0.0505` n `27`; metal avg `-0.0087` n `20`; unknown avg `20.3123` n `1256`
- 4h: commodity avg `-0.6447` n `13`; crypto_alt avg `-0.8491` n `239`; crypto_major avg `-0.1444` n `8`; equity avg `-0.0857` n `161`; fx avg `-0.0062` n `6`; index avg `0.041` n `27`; metal avg `-0.2074` n `20`; unknown avg `2.2128` n `1245`
- 24h: commodity avg `0.1432` n `13`; crypto_alt avg `0.579` n `239`; crypto_major avg `1.0261` n `8`; equity avg `5.5111` n `161`; fx avg `-0.1446` n `6`; index avg `0.5429` n `27`; metal avg `0.0019` n `20`; unknown avg `6.8926` n `1153`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
