# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T08:22:33.237478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `-0.1771` n `228`; crypto_major avg `-0.2326` n `8`; equity avg `-0.0705` n `86`; fx avg `0.0149` n `6`; index avg `-0.0125` n `23`; metal avg `0.061` n `20`; unknown avg `-0.0293` n `765`
- 1h: commodity avg `-0.0778` n `12`; crypto_alt avg `-0.1522` n `228`; crypto_major avg `-0.1405` n `8`; equity avg `-0.1087` n `86`; fx avg `0.0111` n `6`; index avg `-0.0043` n `23`; metal avg `0.0169` n `20`; unknown avg `-0.0395` n `765`
- 4h: commodity avg `-0.0505` n `12`; crypto_alt avg `0.8805` n `228`; crypto_major avg `1.0544` n `8`; equity avg `0.5009` n `86`; fx avg `-0.0401` n `6`; index avg `0.1334` n `23`; metal avg `0.544` n `20`; unknown avg `0.3022` n `733`
- 24h: commodity avg `0.0389` n `12`; crypto_alt avg `-1.6939` n `228`; crypto_major avg `-1.5397` n `8`; equity avg `-3.7848` n `86`; fx avg `0.0485` n `6`; index avg `-0.5412` n `23`; metal avg `0.3824` n `20`; unknown avg `0.5772` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
