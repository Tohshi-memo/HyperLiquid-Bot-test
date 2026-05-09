# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T14:22:14.196646+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0999` n `12`; crypto_alt avg `0.0465` n `228`; crypto_major avg `-0.0238` n `8`; equity avg `-0.0698` n `65`; fx avg `-0.0006` n `5`; index avg `0.0019` n `23`; metal avg `-0.0126` n `18`; unknown avg `0.0184` n `376`
- 1h: commodity avg `0.1592` n `12`; crypto_alt avg `-0.0099` n `228`; crypto_major avg `-0.0334` n `8`; equity avg `-0.1091` n `65`; fx avg `-0.0013` n `5`; index avg `0.0304` n `23`; metal avg `-0.0209` n `18`; unknown avg `-0.1239` n `376`
- 4h: commodity avg `0.2187` n `12`; crypto_alt avg `-0.3297` n `228`; crypto_major avg `-0.0755` n `8`; equity avg `-0.0303` n `65`; fx avg `-0.0032` n `5`; index avg `0.0321` n `23`; metal avg `-0.01` n `18`; unknown avg `-0.3878` n `376`
- 24h: commodity avg `-0.2325` n `12`; crypto_alt avg `1.9414` n `228`; crypto_major avg `1.4327` n `8`; equity avg `1.5957` n `65`; fx avg `0.006` n `5`; index avg `0.659` n `23`; metal avg `-0.1012` n `18`; unknown avg `0.0596` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
