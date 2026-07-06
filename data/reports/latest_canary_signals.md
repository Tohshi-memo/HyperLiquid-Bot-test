# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T09:07:26.279229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0493` n `12`; crypto_alt avg `0.0415` n `229`; crypto_major avg `-0.0066` n `8`; equity avg `0.0288` n `88`; fx avg `0.0042` n `6`; index avg `-0.0047` n `25`; metal avg `0.0098` n `20`; unknown avg `-0.0406` n `765`
- 1h: commodity avg `0.0951` n `12`; crypto_alt avg `-0.3729` n `229`; crypto_major avg `-0.5277` n `8`; equity avg `-0.1025` n `88`; fx avg `0.0113` n `6`; index avg `-0.0321` n `25`; metal avg `-0.1688` n `20`; unknown avg `-0.1231` n `765`
- 4h: commodity avg `0.0273` n `12`; crypto_alt avg `-0.4708` n `229`; crypto_major avg `-0.504` n `8`; equity avg `0.0609` n `88`; fx avg `0.0319` n `6`; index avg `0.0449` n `25`; metal avg `0.0969` n `20`; unknown avg `-0.2689` n `731`
- 24h: commodity avg `-0.2157` n `12`; crypto_alt avg `-0.4085` n `229`; crypto_major avg `0.4804` n `8`; equity avg `-0.5858` n `88`; fx avg `0.0863` n `6`; index avg `-0.0092` n `25`; metal avg `-0.1849` n `20`; unknown avg `1.0312` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
