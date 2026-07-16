# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T10:22:25.819712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `12`; crypto_alt avg `0.0778` n `230`; crypto_major avg `-0.0126` n `8`; equity avg `-0.1168` n `94`; fx avg `0.0008` n `6`; index avg `-0.014` n `25`; metal avg `-0.0151` n `20`; unknown avg `0.0198` n `768`
- 1h: commodity avg `0.1231` n `12`; crypto_alt avg `0.1064` n `230`; crypto_major avg `0.1007` n `8`; equity avg `-0.3863` n `94`; fx avg `-0.0194` n `6`; index avg `-0.0776` n `25`; metal avg `-0.053` n `20`; unknown avg `-0.0083` n `768`
- 4h: commodity avg `0.0378` n `12`; crypto_alt avg `-0.8127` n `230`; crypto_major avg `-1.0287` n `8`; equity avg `-0.9002` n `94`; fx avg `-0.0801` n `6`; index avg `-0.1268` n `25`; metal avg `-0.073` n `20`; unknown avg `-0.0719` n `762`
- 24h: commodity avg `-0.1227` n `12`; crypto_alt avg `-0.684` n `230`; crypto_major avg `-0.8007` n `8`; equity avg `-2.973` n `93`; fx avg `0.0441` n `6`; index avg `-0.4933` n `25`; metal avg `-0.0104` n `20`; unknown avg `-0.0371` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
