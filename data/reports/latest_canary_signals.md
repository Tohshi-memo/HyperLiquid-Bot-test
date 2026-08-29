# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T23:28:54.337077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `-0.0204` n `231`; crypto_major avg `-0.0008` n `8`; equity avg `0.0034` n `128`; fx avg `0.0027` n `6`; index avg `0.0263` n `26`; metal avg `0.0052` n `20`; unknown avg `0.1115` n `793`
- 1h: commodity avg `-0.0018` n `12`; crypto_alt avg `0.1686` n `231`; crypto_major avg `0.2015` n `8`; equity avg `0.0187` n `128`; fx avg `0.0039` n `6`; index avg `0.0326` n `26`; metal avg `0.0097` n `20`; unknown avg `0.073` n `789`
- 4h: commodity avg `-0.0104` n `12`; crypto_alt avg `-0.1013` n `231`; crypto_major avg `0.0025` n `8`; equity avg `0.1491` n `128`; fx avg `0.0016` n `6`; index avg `0.0462` n `26`; metal avg `0.0117` n `20`; unknown avg `0.4482` n `774`
- 24h: commodity avg `-0.0029` n `12`; crypto_alt avg `0.3527` n `231`; crypto_major avg `0.9439` n `8`; equity avg `0.44` n `128`; fx avg `-0.0207` n `6`; index avg `0.1109` n `26`; metal avg `0.1359` n `20`; unknown avg `0.1702` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2149`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
