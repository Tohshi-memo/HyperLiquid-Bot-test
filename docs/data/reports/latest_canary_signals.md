# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T11:07:32.163591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0158` n `12`; crypto_alt avg `-0.0471` n `229`; crypto_major avg `-0.005` n `8`; equity avg `-0.0823` n `88`; fx avg `-0.0025` n `6`; index avg `-0.0087` n `25`; metal avg `-0.0398` n `20`; unknown avg `-0.0354` n `765`
- 1h: commodity avg `-0.0673` n `12`; crypto_alt avg `0.2512` n `229`; crypto_major avg `0.24` n `8`; equity avg `-0.1344` n `88`; fx avg `-0.0078` n `6`; index avg `-0.0033` n `25`; metal avg `0.1152` n `20`; unknown avg `-0.0478` n `765`
- 4h: commodity avg `-0.083` n `12`; crypto_alt avg `0.3391` n `229`; crypto_major avg `0.0259` n `8`; equity avg `-0.153` n `88`; fx avg `-0.0148` n `6`; index avg `-0.0003` n `25`; metal avg `0.1302` n `20`; unknown avg `-0.0752` n `765`
- 24h: commodity avg `-0.1914` n `12`; crypto_alt avg `0.3808` n `229`; crypto_major avg `0.8867` n `8`; equity avg `-0.8164` n `88`; fx avg `0.0721` n `6`; index avg `-0.0119` n `25`; metal avg `-0.1839` n `20`; unknown avg `0.9799` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
