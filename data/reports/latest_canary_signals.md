# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T19:52:29.715781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0072` n `12`; crypto_alt avg `0.034` n `228`; crypto_major avg `0.017` n `8`; equity avg `0.0633` n `86`; fx avg `-0.0117` n `6`; index avg `0.0512` n `23`; metal avg `0.065` n `20`; unknown avg `2.799` n `764`
- 1h: commodity avg `0.0385` n `12`; crypto_alt avg `0.4275` n `228`; crypto_major avg `0.3552` n `8`; equity avg `0.3529` n `86`; fx avg `-0.0067` n `6`; index avg `0.1151` n `23`; metal avg `0.1071` n `20`; unknown avg `0.1337` n `764`
- 4h: commodity avg `-0.0287` n `12`; crypto_alt avg `-1.5267` n `228`; crypto_major avg `-1.0561` n `8`; equity avg `-1.2413` n `86`; fx avg `0.0119` n `6`; index avg `-0.116` n `23`; metal avg `-0.5925` n `20`; unknown avg `-0.8166` n `764`
- 24h: commodity avg `-0.5524` n `12`; crypto_alt avg `-3.8823` n `228`; crypto_major avg `-3.6174` n `8`; equity avg `2.0833` n `86`; fx avg `0.0558` n `6`; index avg `0.0832` n `23`; metal avg `-1.9232` n `20`; unknown avg `-0.6442` n `724`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
