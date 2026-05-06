# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T11:52:25.071014+00:00`
- Correlation status: `ready`
- Asset price records: `451`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.9034` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.5579` n `7`; crypto_alt avg `-0.2221` n `223`; crypto_major avg `-0.0533` n `7`; equity avg `-0.3148` n `47`; fx avg `0.039` n `4`; index avg `0.1201` n `6`; metal avg `-0.3914` n `7`; unknown avg `-0.01` n `313`
- 1h: commodity avg `0.0959` n `7`; crypto_alt avg `-0.1839` n `223`; crypto_major avg `0.3963` n `7`; equity avg `0.0385` n `47`; fx avg `0.0731` n `4`; index avg `0.3901` n `6`; metal avg `-0.4241` n `7`; unknown avg `0.0709` n `313`
- 4h: commodity avg `-2.4949` n `7`; crypto_alt avg `1.126` n `223`; crypto_major avg `1.4085` n `7`; equity avg `1.1926` n `47`; fx avg `-0.1399` n `4`; index avg `1.4576` n `6`; metal avg `0.9424` n `7`; unknown avg `0.1353` n `313`
- 24h: commodity avg `-3.9015` n `7`; crypto_alt avg `3.6735` n `223`; crypto_major avg `3.1173` n `7`; equity avg `3.6188` n `47`; fx avg `-0.608` n `4`; index avg `3.4773` n `6`; metal avg `2.6428` n `7`; unknown avg `2.0853` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1671`, n `447`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.161`, n `447`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1509`, n `447`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1394`, n `447`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1196`, n `447`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.116`, n `447`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1157`, n `443`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1117`, n `443`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0984`, n `443`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `443`, weak_sample_signal
