# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T01:07:27.231990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `13`; crypto_alt avg `-0.2001` n `239`; crypto_major avg `-0.1742` n `8`; equity avg `0.0596` n `166`; fx avg `0.0011` n `6`; index avg `0.0265` n `27`; metal avg `0.0134` n `20`; unknown avg `1.1174` n `1252`
- 1h: commodity avg `0.0128` n `13`; crypto_alt avg `-0.2459` n `239`; crypto_major avg `-0.1125` n `8`; equity avg `0.1958` n `166`; fx avg `0.0044` n `6`; index avg `0.0227` n `27`; metal avg `0.0269` n `20`; unknown avg `-0.0921` n `1256`
- 4h: commodity avg `-0.0379` n `13`; crypto_alt avg `1.1931` n `239`; crypto_major avg `1.4846` n `8`; equity avg `1.1673` n `166`; fx avg `-0.0197` n `6`; index avg `0.1195` n `27`; metal avg `0.1613` n `20`; unknown avg `163.7536` n `1228`
- 24h: commodity avg `0.353` n `13`; crypto_alt avg `-5.396` n `239`; crypto_major avg `-6.0965` n `8`; equity avg `-5.6283` n `166`; fx avg `-0.0276` n `6`; index avg `-0.61` n `27`; metal avg `-0.4995` n `20`; unknown avg `12.9009` n `1115`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
