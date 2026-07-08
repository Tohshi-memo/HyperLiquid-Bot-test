# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T18:07:30.760597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `-0.0554` n `229`; crypto_major avg `-0.0911` n `8`; equity avg `0.0786` n `91`; fx avg `0.0067` n `6`; index avg `0.0139` n `25`; metal avg `0.0019` n `20`; unknown avg `-0.0174` n `764`
- 1h: commodity avg `-0.1651` n `12`; crypto_alt avg `-0.0463` n `229`; crypto_major avg `0.0933` n `8`; equity avg `0.2683` n `91`; fx avg `0.0097` n `6`; index avg `0.0263` n `25`; metal avg `0.0504` n `20`; unknown avg `0.0009` n `764`
- 4h: commodity avg `-0.2265` n `12`; crypto_alt avg `0.0983` n `229`; crypto_major avg `0.2006` n `8`; equity avg `0.0052` n `91`; fx avg `0.0443` n `6`; index avg `0.1221` n `25`; metal avg `-0.0204` n `20`; unknown avg `-0.1127` n `764`
- 24h: commodity avg `0.6319` n `12`; crypto_alt avg `-3.1683` n `229`; crypto_major avg `-3.6027` n `8`; equity avg `-0.1955` n `91`; fx avg `0.0296` n `6`; index avg `-0.2033` n `25`; metal avg `-1.2236` n `20`; unknown avg `-0.5438` n `737`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0509`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
