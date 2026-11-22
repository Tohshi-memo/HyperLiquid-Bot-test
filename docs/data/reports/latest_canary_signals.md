# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T14:22:33.468803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `13`; crypto_alt avg `-0.2119` n `239`; crypto_major avg `-0.0836` n `8`; equity avg `0.0094` n `166`; fx avg `-0.0033` n `6`; index avg `-0.0012` n `27`; metal avg `-0.0009` n `20`; unknown avg `-0.1361` n `1261`
- 1h: commodity avg `-0.0093` n `13`; crypto_alt avg `0.041` n `239`; crypto_major avg `0.002` n `8`; equity avg `0.0344` n `166`; fx avg `-0.0039` n `6`; index avg `0.0411` n `27`; metal avg `-0.0046` n `20`; unknown avg `158.7935` n `1259`
- 4h: commodity avg `-0.0253` n `13`; crypto_alt avg `-0.0123` n `239`; crypto_major avg `-0.3132` n `8`; equity avg `0.0971` n `166`; fx avg `-0.0014` n `6`; index avg `0.0341` n `27`; metal avg `0.0013` n `20`; unknown avg `373.9246` n `1253`
- 24h: commodity avg `-0.043` n `13`; crypto_alt avg `0.6248` n `239`; crypto_major avg `0.3802` n `8`; equity avg `0.933` n `166`; fx avg `-0.0089` n `6`; index avg `0.1456` n `27`; metal avg `0.0031` n `20`; unknown avg `0.193` n `1084`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
