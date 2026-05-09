# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T16:22:19.904925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.019` n `12`; crypto_alt avg `0.3941` n `228`; crypto_major avg `0.2398` n `8`; equity avg `0.0528` n `65`; fx avg `0.0` n `5`; index avg `0.0224` n `23`; metal avg `0.0344` n `18`; unknown avg `-0.1023` n `376`
- 1h: commodity avg `-0.0573` n `12`; crypto_alt avg `0.361` n `228`; crypto_major avg `0.3917` n `8`; equity avg `0.06` n `65`; fx avg `-0.0303` n `5`; index avg `0.0408` n `23`; metal avg `0.0503` n `18`; unknown avg `-0.195` n `376`
- 4h: commodity avg `0.4117` n `12`; crypto_alt avg `-0.5864` n `228`; crypto_major avg `-0.2369` n `8`; equity avg `0.1163` n `65`; fx avg `-0.0138` n `5`; index avg `0.0844` n `23`; metal avg `-0.0649` n `18`; unknown avg `-0.1975` n `376`
- 24h: commodity avg `-0.629` n `12`; crypto_alt avg `1.3836` n `228`; crypto_major avg `1.3936` n `8`; equity avg `1.678` n `65`; fx avg `-0.0008` n `5`; index avg `0.6702` n `23`; metal avg `0.0703` n `18`; unknown avg `0.2209` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
