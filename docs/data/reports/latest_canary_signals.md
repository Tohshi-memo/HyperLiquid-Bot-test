# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T20:52:25.262230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0096` n `12`; crypto_alt avg `-0.0512` n `230`; crypto_major avg `-0.0122` n `8`; equity avg `0.0176` n `92`; fx avg `0.0038` n `6`; index avg `-0.0` n `25`; metal avg `0.0027` n `20`; unknown avg `0.0404` n `765`
- 1h: commodity avg `0.0133` n `12`; crypto_alt avg `0.0917` n `230`; crypto_major avg `0.0922` n `8`; equity avg `0.0207` n `92`; fx avg `0.0026` n `6`; index avg `-0.0092` n `25`; metal avg `0.0062` n `20`; unknown avg `-0.0069` n `765`
- 4h: commodity avg `0.0656` n `12`; crypto_alt avg `0.3639` n `230`; crypto_major avg `0.3998` n `8`; equity avg `0.2152` n `92`; fx avg `0.0279` n `6`; index avg `0.0012` n `25`; metal avg `0.0019` n `20`; unknown avg `0.0355` n `765`
- 24h: commodity avg `0.0012` n `12`; crypto_alt avg `1.3364` n `229`; crypto_major avg `1.0033` n `8`; equity avg `0.3805` n `92`; fx avg `0.0173` n `6`; index avg `0.0132` n `25`; metal avg `-0.0224` n `20`; unknown avg `2.3198` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
