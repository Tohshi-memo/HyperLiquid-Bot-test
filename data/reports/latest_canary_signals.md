# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T16:22:29.363104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `-0.0063` n `229`; crypto_major avg `0.0554` n `8`; equity avg `-0.0238` n `88`; fx avg `-0.0092` n `6`; index avg `-0.0052` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.227` n `765`
- 1h: commodity avg `0.027` n `12`; crypto_alt avg `0.2787` n `229`; crypto_major avg `0.0425` n `8`; equity avg `-0.0037` n `88`; fx avg `-0.0034` n `6`; index avg `-0.0041` n `25`; metal avg `0.0133` n `20`; unknown avg `0.2476` n `765`
- 4h: commodity avg `-0.0174` n `12`; crypto_alt avg `0.8679` n `229`; crypto_major avg `0.9486` n `8`; equity avg `0.0735` n `88`; fx avg `0.0167` n `6`; index avg `0.0098` n `25`; metal avg `0.0296` n `20`; unknown avg `0.295` n `759`
- 24h: commodity avg `0.0227` n `12`; crypto_alt avg `1.5674` n `229`; crypto_major avg `1.8371` n `8`; equity avg `0.2544` n `88`; fx avg `-0.022` n `6`; index avg `-0.0158` n `25`; metal avg `0.0856` n `20`; unknown avg `1.7859` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
