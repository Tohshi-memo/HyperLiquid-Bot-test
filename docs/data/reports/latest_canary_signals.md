# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T12:22:26.298829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `0.1134` n `230`; crypto_major avg `0.2012` n `8`; equity avg `0.037` n `121`; fx avg `0.0014` n `6`; index avg `0.0049` n `25`; metal avg `-0.0019` n `20`; unknown avg `0.1321` n `795`
- 1h: commodity avg `0.0069` n `12`; crypto_alt avg `0.2071` n `230`; crypto_major avg `-0.0333` n `8`; equity avg `0.07` n `121`; fx avg `-0.0016` n `6`; index avg `0.0164` n `25`; metal avg `0.0143` n `20`; unknown avg `0.9096` n `795`
- 4h: commodity avg `-0.0219` n `12`; crypto_alt avg `2.1603` n `230`; crypto_major avg `1.0803` n `8`; equity avg `0.2682` n `121`; fx avg `0.0029` n `6`; index avg `0.043` n `25`; metal avg `0.0154` n `20`; unknown avg `2.3245` n `794`
- 24h: commodity avg `-0.0014` n `12`; crypto_alt avg `-0.3625` n `230`; crypto_major avg `0.0328` n `8`; equity avg `0.4195` n `121`; fx avg `0.0355` n `6`; index avg `0.0427` n `25`; metal avg `0.0534` n `20`; unknown avg `3.7668` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
