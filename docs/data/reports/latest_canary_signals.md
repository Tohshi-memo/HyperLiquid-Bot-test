# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T21:07:27.999327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0386` n `13`; crypto_alt avg `-0.09` n `239`; crypto_major avg `-0.1995` n `8`; equity avg `0.1998` n `162`; fx avg `-0.0061` n `6`; index avg `0.028` n `27`; metal avg `-0.0249` n `20`; unknown avg `0.759` n `1241`
- 1h: commodity avg `-0.004` n `13`; crypto_alt avg `0.2204` n `239`; crypto_major avg `0.0123` n `8`; equity avg `0.2012` n `162`; fx avg `0.0078` n `6`; index avg `0.0324` n `27`; metal avg `-0.0616` n `20`; unknown avg `0.1904` n `1233`
- 4h: commodity avg `0.5868` n `13`; crypto_alt avg `0.8245` n `239`; crypto_major avg `0.3044` n `8`; equity avg `-0.2564` n `162`; fx avg `0.0185` n `6`; index avg `-0.0168` n `27`; metal avg `-0.0384` n `20`; unknown avg `6.6662` n `1223`
- 24h: commodity avg `0.9051` n `13`; crypto_alt avg `-2.3838` n `239`; crypto_major avg `-3.1592` n `8`; equity avg `-2.389` n `162`; fx avg `-0.1315` n `6`; index avg `-0.1089` n `27`; metal avg `-0.7421` n `20`; unknown avg `14.128` n `1147`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
