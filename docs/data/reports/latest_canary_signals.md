# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T21:37:35.996782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0856` n `13`; crypto_alt avg `0.1145` n `239`; crypto_major avg `-0.038` n `8`; equity avg `0.2148` n `160`; fx avg `-0.0035` n `6`; index avg `0.0191` n `27`; metal avg `0.0258` n `20`; unknown avg `1.3098` n `1261`
- 1h: commodity avg `-0.0256` n `13`; crypto_alt avg `-0.1888` n `239`; crypto_major avg `-0.0125` n `8`; equity avg `-0.2492` n `160`; fx avg `0.0201` n `6`; index avg `-0.0264` n `27`; metal avg `-0.0375` n `20`; unknown avg `4.9041` n `1221`
- 4h: commodity avg `-0.1996` n `13`; crypto_alt avg `-0.0066` n `239`; crypto_major avg `0.1393` n `8`; equity avg `0.2294` n `160`; fx avg `-0.0077` n `6`; index avg `0.0631` n `27`; metal avg `0.2969` n `20`; unknown avg `4.3655` n `1211`
- 24h: commodity avg `-0.4602` n `13`; crypto_alt avg `0.6409` n `239`; crypto_major avg `-2.0548` n `8`; equity avg `4.4417` n `160`; fx avg `-0.1301` n `6`; index avg `0.5926` n `27`; metal avg `0.6691` n `20`; unknown avg `4.2388` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
