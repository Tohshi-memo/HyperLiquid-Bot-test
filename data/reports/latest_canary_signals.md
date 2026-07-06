# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T07:37:29.504301+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0681` n `12`; crypto_alt avg `0.1095` n `229`; crypto_major avg `0.1369` n `8`; equity avg `-0.0299` n `88`; fx avg `-0.0075` n `6`; index avg `-0.0008` n `25`; metal avg `0.0483` n `20`; unknown avg `-0.0388` n `765`
- 1h: commodity avg `-0.1322` n `12`; crypto_alt avg `0.241` n `229`; crypto_major avg `0.2375` n `8`; equity avg `0.0072` n `88`; fx avg `0.0192` n `6`; index avg `0.0164` n `25`; metal avg `0.1031` n `20`; unknown avg `0.0263` n `765`
- 4h: commodity avg `0.1066` n `12`; crypto_alt avg `-0.6263` n `229`; crypto_major avg `-0.3647` n `8`; equity avg `0.1225` n `88`; fx avg `0.0284` n `6`; index avg `0.0854` n `25`; metal avg `0.0308` n `20`; unknown avg `-0.13` n `731`
- 24h: commodity avg `-0.1556` n `12`; crypto_alt avg `0.0207` n `229`; crypto_major avg `0.9514` n `8`; equity avg `-0.6512` n `88`; fx avg `0.0866` n `6`; index avg `-0.0167` n `25`; metal avg `-0.1244` n `20`; unknown avg `1.0504` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
