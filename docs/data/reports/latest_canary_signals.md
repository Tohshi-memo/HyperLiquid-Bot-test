# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T14:37:14.106732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `-0.3344` n `228`; crypto_major avg `-0.267` n `8`; equity avg `0.0367` n `65`; fx avg `0.0` n `5`; index avg `-0.0593` n `23`; metal avg `-0.0254` n `18`; unknown avg `0.0954` n `376`
- 1h: commodity avg `0.1698` n `12`; crypto_alt avg `-0.4233` n `228`; crypto_major avg `-0.3368` n `8`; equity avg `-0.0867` n `65`; fx avg `0.0174` n `5`; index avg `-0.0477` n `23`; metal avg `-0.0321` n `18`; unknown avg `-0.0242` n `376`
- 4h: commodity avg `0.2088` n `12`; crypto_alt avg `-0.7289` n `228`; crypto_major avg `-0.3973` n `8`; equity avg `-0.0389` n `65`; fx avg `-0.0032` n `5`; index avg `-0.0298` n `23`; metal avg `-0.0409` n `18`; unknown avg `-0.4585` n `376`
- 24h: commodity avg `-0.2176` n `12`; crypto_alt avg `1.604` n `228`; crypto_major avg `1.3112` n `8`; equity avg `2.0315` n `65`; fx avg `0.0035` n `5`; index avg `0.768` n `23`; metal avg `-0.0965` n `18`; unknown avg `0.2745` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
