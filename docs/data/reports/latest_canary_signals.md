# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T10:37:30.449527+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `13`; crypto_alt avg `-0.167` n `237`; crypto_major avg `-0.1329` n `8`; equity avg `-0.1015` n `152`; fx avg `0.0009` n `6`; index avg `-0.0085` n `26`; metal avg `-0.0175` n `20`; unknown avg `0.331` n `1233`
- 1h: commodity avg `-0.0393` n `13`; crypto_alt avg `0.1176` n `237`; crypto_major avg `0.1792` n `8`; equity avg `-0.0704` n `152`; fx avg `0.0173` n `6`; index avg `0.0053` n `26`; metal avg `0.006` n `20`; unknown avg `-0.2062` n `1231`
- 4h: commodity avg `0.037` n `13`; crypto_alt avg `-0.1777` n `237`; crypto_major avg `-0.0724` n `8`; equity avg `-0.3502` n `152`; fx avg `-0.0663` n `6`; index avg `-0.0969` n `26`; metal avg `-0.079` n `20`; unknown avg `-0.1968` n `1151`
- 24h: commodity avg `0.3324` n `13`; crypto_alt avg `-0.1814` n `237`; crypto_major avg `0.0242` n `8`; equity avg `-1.4396` n `152`; fx avg `-0.0465` n `6`; index avg `-0.1885` n `26`; metal avg `-0.5043` n `20`; unknown avg `49.5984` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2063`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1866`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
