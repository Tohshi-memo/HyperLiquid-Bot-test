# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T10:52:26.108587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `-0.0564` n `230`; crypto_major avg `-0.0632` n `8`; equity avg `-0.05` n `94`; fx avg `-0.0016` n `6`; index avg `-0.0092` n `25`; metal avg `-0.0265` n `20`; unknown avg `-0.0366` n `768`
- 1h: commodity avg `0.0697` n `12`; crypto_alt avg `0.1147` n `230`; crypto_major avg `0.0489` n `8`; equity avg `-0.1414` n `94`; fx avg `-0.0129` n `6`; index avg `-0.0301` n `25`; metal avg `-0.0649` n `20`; unknown avg `-0.0341` n `768`
- 4h: commodity avg `0.0969` n `12`; crypto_alt avg `-0.8205` n `230`; crypto_major avg `-1.0796` n `8`; equity avg `-0.7764` n `94`; fx avg `-0.0361` n `6`; index avg `-0.1091` n `25`; metal avg `-0.0542` n `20`; unknown avg `-0.2249` n `762`
- 24h: commodity avg `-0.0803` n `12`; crypto_alt avg `-0.639` n `230`; crypto_major avg `-0.7322` n `8`; equity avg `-2.8973` n `93`; fx avg `0.0473` n `6`; index avg `-0.4805` n `25`; metal avg `0.0464` n `20`; unknown avg `-0.0547` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
