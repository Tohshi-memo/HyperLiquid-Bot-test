# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T19:39:57.561150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `12`; crypto_alt avg `-0.0426` n `229`; crypto_major avg `0.0376` n `8`; equity avg `0.0079` n `88`; fx avg `0.0328` n `6`; index avg `0.0006` n `25`; metal avg `0.0084` n `20`; unknown avg `0.0403` n `765`
- 1h: commodity avg `-0.0247` n `12`; crypto_alt avg `0.145` n `229`; crypto_major avg `0.1751` n `8`; equity avg `0.0329` n `88`; fx avg `0.0095` n `6`; index avg `0.0029` n `25`; metal avg `0.0091` n `20`; unknown avg `0.7043` n `765`
- 4h: commodity avg `-0.0072` n `12`; crypto_alt avg `0.3206` n `229`; crypto_major avg `0.1388` n `8`; equity avg `0.0958` n `88`; fx avg `0.0239` n `6`; index avg `0.0225` n `25`; metal avg `0.0066` n `20`; unknown avg `0.7481` n `713`
- 24h: commodity avg `0.026` n `12`; crypto_alt avg `-1.1476` n `229`; crypto_major avg `-0.5568` n `8`; equity avg `0.3188` n `88`; fx avg `-0.0271` n `6`; index avg `0.1021` n `25`; metal avg `0.0278` n `20`; unknown avg `0.9017` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
