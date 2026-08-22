# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T18:07:24.492164+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `12`; crypto_alt avg `-0.21` n `230`; crypto_major avg `-0.0461` n `8`; equity avg `0.0109` n `121`; fx avg `0.0012` n `6`; index avg `0.0013` n `25`; metal avg `0.0034` n `20`; unknown avg `-0.0515` n `794`
- 1h: commodity avg `0.0025` n `12`; crypto_alt avg `0.1563` n `230`; crypto_major avg `0.3797` n `8`; equity avg `0.0427` n `121`; fx avg `-0.0057` n `6`; index avg `0.0009` n `25`; metal avg `0.0071` n `20`; unknown avg `0.2012` n `794`
- 4h: commodity avg `0.015` n `12`; crypto_alt avg `0.9655` n `230`; crypto_major avg `0.9649` n `8`; equity avg `0.0196` n `121`; fx avg `0.0261` n `6`; index avg `0.0044` n `25`; metal avg `0.0142` n `20`; unknown avg `0.5272` n `794`
- 24h: commodity avg `-0.1195` n `12`; crypto_alt avg `0.6313` n `230`; crypto_major avg `3.277` n `8`; equity avg `-0.3994` n `121`; fx avg `0.0343` n `6`; index avg `-0.0478` n `25`; metal avg `-0.1327` n `20`; unknown avg `2.0787` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
