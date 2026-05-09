# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T10:07:12.040680+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `-0.0663` n `228`; crypto_major avg `-0.0629` n `8`; equity avg `0.0479` n `65`; fx avg `0.0` n `5`; index avg `-0.002` n `23`; metal avg `-0.021` n `18`; unknown avg `0.2398` n `376`
- 1h: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.7705` n `228`; crypto_major avg `-0.4153` n `8`; equity avg `-0.004` n `65`; fx avg `0.0` n `5`; index avg `-0.0562` n `23`; metal avg `-0.033` n `18`; unknown avg `0.0282` n `376`
- 4h: commodity avg `0.0277` n `12`; crypto_alt avg `-1.3572` n `228`; crypto_major avg `-0.6321` n `8`; equity avg `0.0597` n `65`; fx avg `0.0023` n `5`; index avg `0.0417` n `23`; metal avg `-0.0292` n `18`; unknown avg `-0.4379` n `376`
- 24h: commodity avg `-0.2201` n `12`; crypto_alt avg `2.7937` n `228`; crypto_major avg `1.9099` n `8`; equity avg `2.7834` n `65`; fx avg `-0.0441` n `5`; index avg `1.1296` n `23`; metal avg `-0.0517` n `18`; unknown avg `0.3972` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
