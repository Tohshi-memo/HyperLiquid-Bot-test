# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T17:22:25.655420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `0.0171` n `229`; crypto_major avg `-0.0046` n `8`; equity avg `-0.0117` n `88`; fx avg `0.004` n `6`; index avg `-0.0121` n `25`; metal avg `0.0` n `20`; unknown avg `0.091` n `765`
- 1h: commodity avg `0.0081` n `12`; crypto_alt avg `0.2025` n `229`; crypto_major avg `0.0868` n `8`; equity avg `0.0188` n `88`; fx avg `0.0327` n `6`; index avg `-0.0024` n `25`; metal avg `0.0014` n `20`; unknown avg `0.067` n `765`
- 4h: commodity avg `0.0036` n `12`; crypto_alt avg `0.1589` n `229`; crypto_major avg `0.2981` n `8`; equity avg `-0.0264` n `88`; fx avg `-0.0295` n `6`; index avg `0.0214` n `25`; metal avg `-0.0209` n `20`; unknown avg `0.1918` n `695`
- 24h: commodity avg `0.0065` n `12`; crypto_alt avg `-1.6231` n `229`; crypto_major avg `-0.8073` n `8`; equity avg `0.2689` n `88`; fx avg `-0.0756` n `6`; index avg `0.1101` n `25`; metal avg `0.0611` n `20`; unknown avg `-0.0049` n `663`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
