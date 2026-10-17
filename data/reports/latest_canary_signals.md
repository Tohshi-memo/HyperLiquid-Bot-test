# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T12:52:27.279954+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `13`; crypto_alt avg `-0.463` n `236`; crypto_major avg `-0.1908` n `8`; equity avg `-0.0564` n `151`; fx avg `-0.0036` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0083` n `20`; unknown avg `-0.1194` n `1193`
- 1h: commodity avg `-0.0182` n `13`; crypto_alt avg `-0.8561` n `236`; crypto_major avg `-0.4303` n `8`; equity avg `-0.1623` n `151`; fx avg `0.0007` n `6`; index avg `-0.0374` n `26`; metal avg `-0.0214` n `20`; unknown avg `2.9141` n `1185`
- 4h: commodity avg `-0.018` n `13`; crypto_alt avg `-1.2127` n `236`; crypto_major avg `-0.6942` n `8`; equity avg `-0.1559` n `151`; fx avg `0.0195` n `6`; index avg `-0.0184` n `26`; metal avg `-0.0172` n `20`; unknown avg `3.0764` n `1183`
- 24h: commodity avg `0.5231` n `13`; crypto_alt avg `-3.0621` n `236`; crypto_major avg `-1.7162` n `8`; equity avg `-3.2824` n `151`; fx avg `0.0301` n `6`; index avg `-0.5554` n `26`; metal avg `-0.1894` n `20`; unknown avg `10.4167` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1767`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1462`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.119`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1166`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0678`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0636`, n `666`, weak_sample_signal
