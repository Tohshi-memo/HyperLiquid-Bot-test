# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T09:22:40.483389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0605` n `12`; crypto_alt avg `0.0461` n `228`; crypto_major avg `0.126` n `8`; equity avg `-0.0273` n `88`; fx avg `-0.0172` n `6`; index avg `0.0092` n `25`; metal avg `-0.0224` n `20`; unknown avg `0.447` n `763`
- 1h: commodity avg `-0.1281` n `12`; crypto_alt avg `0.1151` n `228`; crypto_major avg `0.2688` n `8`; equity avg `0.2561` n `88`; fx avg `-0.0016` n `6`; index avg `0.0296` n `25`; metal avg `0.003` n `20`; unknown avg `1.1227` n `763`
- 4h: commodity avg `-0.1328` n `12`; crypto_alt avg `-0.0344` n `228`; crypto_major avg `-0.1619` n `8`; equity avg `-0.7326` n `88`; fx avg `-0.0654` n `6`; index avg `-0.2038` n `25`; metal avg `0.1139` n `20`; unknown avg `2.2546` n `741`
- 24h: commodity avg `-0.4021` n `12`; crypto_alt avg `2.0296` n `228`; crypto_major avg `1.7673` n `8`; equity avg `-1.9122` n `88`; fx avg `-0.0707` n `6`; index avg `-0.526` n `25`; metal avg `1.1486` n `20`; unknown avg `16.7576` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
