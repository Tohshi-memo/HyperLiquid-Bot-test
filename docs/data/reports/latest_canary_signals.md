# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T21:37:34.228783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `12`; crypto_alt avg `0.0236` n `230`; crypto_major avg `-0.0121` n `8`; equity avg `0.0157` n `102`; fx avg `0.0048` n `6`; index avg `0.0014` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.3168` n `779`
- 1h: commodity avg `-0.0186` n `12`; crypto_alt avg `-0.004` n `230`; crypto_major avg `0.0595` n `8`; equity avg `0.3253` n `102`; fx avg `-0.0149` n `6`; index avg `-0.0017` n `25`; metal avg `0.0094` n `20`; unknown avg `0.0374` n `779`
- 4h: commodity avg `-0.0257` n `12`; crypto_alt avg `0.0706` n `230`; crypto_major avg `0.0145` n `8`; equity avg `1.1672` n `102`; fx avg `0.0199` n `6`; index avg `0.1556` n `25`; metal avg `0.1037` n `20`; unknown avg `-0.044` n `779`
- 24h: commodity avg `-0.2007` n `12`; crypto_alt avg `1.4107` n `230`; crypto_major avg `2.0005` n `8`; equity avg `8.7434` n `102`; fx avg `-0.4075` n `6`; index avg `1.0848` n `25`; metal avg `0.6995` n `20`; unknown avg `0.2383` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
