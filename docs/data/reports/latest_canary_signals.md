# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T16:07:30.532951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `-0.1229` n `229`; crypto_major avg `0.0221` n `8`; equity avg `0.0225` n `88`; fx avg `-0.006` n `6`; index avg `0.0063` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.0858` n `715`
- 1h: commodity avg `0.0015` n `12`; crypto_alt avg `-0.4228` n `229`; crypto_major avg `-0.2507` n `8`; equity avg `-0.0333` n `88`; fx avg `-0.0035` n `6`; index avg `-0.0078` n `25`; metal avg `-0.005` n `20`; unknown avg `0.0995` n `697`
- 4h: commodity avg `0.0054` n `12`; crypto_alt avg `0.5382` n `229`; crypto_major avg `0.9499` n `8`; equity avg `0.0278` n `88`; fx avg `-0.0824` n `6`; index avg `0.0276` n `25`; metal avg `0.005` n `20`; unknown avg `0.3539` n `697`
- 24h: commodity avg `-0.0135` n `12`; crypto_alt avg `-1.8075` n `229`; crypto_major avg `-0.7257` n `8`; equity avg `0.2195` n `88`; fx avg `-0.096` n `6`; index avg `0.0695` n `25`; metal avg `0.0547` n `20`; unknown avg `0.1516` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
