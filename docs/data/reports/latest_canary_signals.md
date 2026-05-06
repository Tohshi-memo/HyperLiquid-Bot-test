# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T11:07:25.744954+00:00`
- Correlation status: `ready`
- Asset price records: `448`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.6717` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.5191` n `7`; crypto_alt avg `0.064` n `223`; crypto_major avg `0.2122` n `7`; equity avg `0.1893` n `47`; fx avg `-0.0112` n `4`; index avg `0.1675` n `6`; metal avg `-0.0596` n `7`; unknown avg `0.3397` n `313`
- 1h: commodity avg `-1.1773` n `7`; crypto_alt avg `0.1145` n `223`; crypto_major avg `0.2693` n `7`; equity avg `0.5532` n `47`; fx avg `-0.112` n `4`; index avg `0.2912` n `6`; metal avg `0.2277` n `7`; unknown avg `0.0615` n `313`
- 4h: commodity avg `-3.3431` n `7`; crypto_alt avg `1.4993` n `223`; crypto_major avg `1.3286` n `7`; equity avg `1.4127` n `47`; fx avg `-0.2775` n `4`; index avg `1.126` n `6`; metal avg `1.5285` n `7`; unknown avg `0.7107` n `313`
- 24h: commodity avg `-4.6242` n `7`; crypto_alt avg `4.0181` n `223`; crypto_major avg `3.069` n `7`; equity avg `3.9437` n `47`; fx avg `-0.6831` n `4`; index avg `3.1745` n `6`; metal avg `3.4492` n `7`; unknown avg `2.2646` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1677`, n `444`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1617`, n `444`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1509`, n `444`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1403`, n `444`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1208`, n `444`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1171`, n `444`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1148`, n `440`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.106`, n `440`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0978`, n `440`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `440`, weak_sample_signal
