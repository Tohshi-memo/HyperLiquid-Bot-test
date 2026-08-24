# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T16:08:35.828436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `0.385` n `231`; crypto_major avg `0.5108` n `8`; equity avg `-0.0214` n `122`; fx avg `-0.0137` n `6`; index avg `-0.0038` n `25`; metal avg `0.0259` n `20`; unknown avg `0.0414` n `793`
- 1h: commodity avg `-0.062` n `12`; crypto_alt avg `-0.0729` n `231`; crypto_major avg `-0.1104` n `8`; equity avg `0.5891` n `122`; fx avg `-0.0259` n `6`; index avg `0.0982` n `25`; metal avg `-0.1279` n `20`; unknown avg `0.0659` n `793`
- 4h: commodity avg `-0.2447` n `12`; crypto_alt avg `0.6998` n `231`; crypto_major avg `0.667` n `8`; equity avg `-0.5492` n `122`; fx avg `-0.0118` n `6`; index avg `-0.1141` n `25`; metal avg `0.0635` n `20`; unknown avg `0.6056` n `793`
- 24h: commodity avg `-0.2486` n `12`; crypto_alt avg `0.2104` n `231`; crypto_major avg `1.1106` n `8`; equity avg `-2.1821` n `122`; fx avg `-0.1309` n `6`; index avg `-0.2714` n `25`; metal avg `0.205` n `20`; unknown avg `3.8897` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
