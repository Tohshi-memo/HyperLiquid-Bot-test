# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T16:52:41.377560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0182` n `12`; crypto_alt avg `0.1198` n `233`; crypto_major avg `0.1107` n `8`; equity avg `0.0307` n `136`; fx avg `-0.0032` n `6`; index avg `-0.0031` n `27`; metal avg `0.0072` n `20`; unknown avg `3.735` n `838`
- 1h: commodity avg `0.0067` n `12`; crypto_alt avg `0.1717` n `233`; crypto_major avg `0.3736` n `8`; equity avg `0.2313` n `136`; fx avg `-0.0027` n `6`; index avg `0.0443` n `27`; metal avg `0.0329` n `20`; unknown avg `9.703` n `830`
- 4h: commodity avg `0.0038` n `12`; crypto_alt avg `0.2524` n `233`; crypto_major avg `0.8051` n `8`; equity avg `0.4088` n `136`; fx avg `0.0031` n `6`; index avg `0.0639` n `27`; metal avg `0.0195` n `20`; unknown avg `2.9775` n `830`
- 24h: commodity avg `0.2879` n `12`; crypto_alt avg `-0.4529` n `233`; crypto_major avg `-1.1206` n `8`; equity avg `-1.5349` n `136`; fx avg `0.0104` n `6`; index avg `-0.2663` n `26`; metal avg `-0.0825` n `20`; unknown avg `1.182` n `708`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
