# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T10:52:29.320135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0581` n `12`; crypto_alt avg `0.0748` n `233`; crypto_major avg `0.1454` n `8`; equity avg `0.0137` n `136`; fx avg `-0.0043` n `6`; index avg `0.0186` n `27`; metal avg `0.0675` n `20`; unknown avg `0.6026` n `908`
- 1h: commodity avg `-0.1605` n `12`; crypto_alt avg `-0.1786` n `233`; crypto_major avg `0.0897` n `8`; equity avg `0.2495` n `136`; fx avg `-0.0296` n `6`; index avg `0.0496` n `27`; metal avg `0.1242` n `20`; unknown avg `1.8617` n `904`
- 4h: commodity avg `-0.0954` n `12`; crypto_alt avg `-0.2378` n `233`; crypto_major avg `0.1551` n `8`; equity avg `0.2957` n `136`; fx avg `0.0241` n `6`; index avg `0.0496` n `27`; metal avg `0.0156` n `20`; unknown avg `0.7306` n `896`
- 24h: commodity avg `-0.027` n `12`; crypto_alt avg `-1.3732` n `233`; crypto_major avg `-0.7208` n `8`; equity avg `0.2231` n `136`; fx avg `0.187` n `6`; index avg `0.0346` n `27`; metal avg `0.0535` n `20`; unknown avg `-0.5105` n `818`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
