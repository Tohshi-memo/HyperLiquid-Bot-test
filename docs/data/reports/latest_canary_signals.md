# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T17:07:27.249056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `0.1301` n `229`; crypto_major avg `0.161` n `8`; equity avg `0.0027` n `88`; fx avg `-0.0017` n `6`; index avg `0.0038` n `25`; metal avg `-0.0056` n `20`; unknown avg `-0.0536` n `765`
- 1h: commodity avg `0.0077` n `12`; crypto_alt avg `0.1561` n `229`; crypto_major avg `-0.1006` n `8`; equity avg `-0.0009` n `88`; fx avg `0.0079` n `6`; index avg `0.007` n `25`; metal avg `-0.0036` n `20`; unknown avg `-0.0775` n `763`
- 4h: commodity avg `0.0245` n `12`; crypto_alt avg `0.0329` n `229`; crypto_major avg `0.1672` n `8`; equity avg `-0.0193` n `88`; fx avg `-0.0328` n `6`; index avg `0.0332` n `25`; metal avg `-0.0173` n `20`; unknown avg `0.0373` n `695`
- 24h: commodity avg `0.0055` n `12`; crypto_alt avg `-1.4782` n `229`; crypto_major avg `-0.6835` n `8`; equity avg `0.3115` n `88`; fx avg `-0.0796` n `6`; index avg `0.1193` n `25`; metal avg `0.0705` n `20`; unknown avg `-0.061` n `663`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
