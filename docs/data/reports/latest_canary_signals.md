# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T07:37:28.274410+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.097` n `12`; crypto_alt avg `-0.0501` n `230`; crypto_major avg `-0.0347` n `8`; equity avg `0.0195` n `92`; fx avg `0.017` n `6`; index avg `0.021` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.0148` n `766`
- 1h: commodity avg `0.1599` n `12`; crypto_alt avg `-0.0987` n `230`; crypto_major avg `-0.1804` n `8`; equity avg `0.0091` n `92`; fx avg `0.0025` n `6`; index avg `0.0359` n `25`; metal avg `-0.0078` n `20`; unknown avg `-0.0363` n `766`
- 4h: commodity avg `0.1649` n `12`; crypto_alt avg `0.5635` n `230`; crypto_major avg `0.2377` n `8`; equity avg `1.3549` n `92`; fx avg `0.0684` n `6`; index avg `0.3244` n `25`; metal avg `0.1793` n `20`; unknown avg `0.0155` n `750`
- 24h: commodity avg `1.3154` n `12`; crypto_alt avg `-0.8343` n `230`; crypto_major avg `-1.0142` n `8`; equity avg `-0.2847` n `92`; fx avg `-0.137` n `6`; index avg `-0.0374` n `25`; metal avg `0.0124` n `20`; unknown avg `-0.2893` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
