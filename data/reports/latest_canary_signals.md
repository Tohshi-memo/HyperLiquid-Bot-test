# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T06:22:35.963700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `13`; crypto_alt avg `-0.0146` n `239`; crypto_major avg `-0.1397` n `8`; equity avg `-0.0576` n `166`; fx avg `0.0014` n `6`; index avg `-0.0077` n `27`; metal avg `0.0168` n `20`; unknown avg `-0.0754` n `1262`
- 1h: commodity avg `0.0976` n `13`; crypto_alt avg `0.0321` n `239`; crypto_major avg `-0.3357` n `8`; equity avg `-0.3314` n `166`; fx avg `0.0107` n `6`; index avg `-0.0468` n `27`; metal avg `-0.1473` n `20`; unknown avg `324.807` n `1232`
- 4h: commodity avg `-0.035` n `13`; crypto_alt avg `0.7718` n `239`; crypto_major avg `0.1616` n `8`; equity avg `-0.3899` n `166`; fx avg `0.0074` n `6`; index avg `-0.0272` n `27`; metal avg `-0.4611` n `20`; unknown avg `164.16` n `1214`
- 24h: commodity avg `-1.1705` n `13`; crypto_alt avg `0.9643` n `239`; crypto_major avg `0.0558` n `8`; equity avg `4.2075` n `166`; fx avg `-0.26` n `6`; index avg `0.6444` n `27`; metal avg `-0.2118` n `20`; unknown avg `306.1552` n `1032`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
