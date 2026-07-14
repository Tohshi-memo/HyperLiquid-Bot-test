# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T06:52:28.302850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0369` n `12`; crypto_alt avg `-0.0153` n `230`; crypto_major avg `-0.0337` n `8`; equity avg `-0.0917` n `92`; fx avg `0.0091` n `6`; index avg `0.004` n `25`; metal avg `0.0225` n `20`; unknown avg `-0.0354` n `766`
- 1h: commodity avg `0.2219` n `12`; crypto_alt avg `0.0884` n `230`; crypto_major avg `-0.1009` n `8`; equity avg `0.1157` n `92`; fx avg `0.0196` n `6`; index avg `-0.0136` n `25`; metal avg `-0.0183` n `20`; unknown avg `-0.0318` n `750`
- 4h: commodity avg `0.1171` n `12`; crypto_alt avg `0.5178` n `230`; crypto_major avg `0.2514` n `8`; equity avg `0.9855` n `92`; fx avg `0.0239` n `6`; index avg `0.2196` n `25`; metal avg `0.2587` n `20`; unknown avg `-0.0092` n `750`
- 24h: commodity avg `1.1809` n `12`; crypto_alt avg `-0.4749` n `230`; crypto_major avg `-0.511` n `8`; equity avg `-0.2332` n `92`; fx avg `-0.1274` n `6`; index avg `-0.0224` n `25`; metal avg `0.1461` n `20`; unknown avg `-0.205` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1633`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
