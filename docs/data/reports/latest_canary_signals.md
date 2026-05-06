# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T11:22:23.986595+00:00`
- Correlation status: `ready`
- Asset price records: `449`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.8157` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.1516` n `7`; crypto_alt avg `-0.0054` n `223`; crypto_major avg `0.2599` n `7`; equity avg `0.137` n `47`; fx avg `0.0339` n `4`; index avg `0.0958` n `6`; metal avg `-0.0184` n `7`; unknown avg `-0.2174` n `313`
- 1h: commodity avg `-1.0961` n `7`; crypto_alt avg `0.1621` n `223`; crypto_major avg `0.544` n `7`; equity avg `0.6322` n `47`; fx avg `-0.0879` n `4`; index avg `0.4058` n `6`; metal avg `0.1921` n `7`; unknown avg `-0.14` n `313`
- 4h: commodity avg `-3.1513` n `7`; crypto_alt avg `1.5249` n `223`; crypto_major avg `1.6644` n `7`; equity avg `1.4778` n `47`; fx avg `-0.2475` n `4`; index avg `1.2222` n `6`; metal avg `1.542` n `7`; unknown avg `0.5055` n `313`
- 24h: commodity avg `-4.619` n `7`; crypto_alt avg `4.2079` n `223`; crypto_major avg `3.3411` n `7`; equity avg `3.9631` n `47`; fx avg `-0.6541` n `4`; index avg `3.3578` n `6`; metal avg `3.2455` n `7`; unknown avg `2.2878` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1675`, n `445`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1615`, n `445`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1514`, n `445`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1409`, n `445`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1202`, n `445`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1166`, n `445`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.116`, n `441`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1089`, n `441`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.099`, n `441`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.097`, n `441`, weak_sample_signal
