# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T15:30:35.028534+00:00`
- Correlation status: `ready`
- Asset price records: `370`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0357` n `7`; crypto_alt avg `-0.0851` n `223`; crypto_major avg `0.0659` n `7`; equity avg `0.1525` n `47`; fx avg `-0.0126` n `4`; index avg `0.0799` n `6`; metal avg `0.0481` n `7`; unknown avg `-0.0141` n `313`
- 1h: commodity avg `-0.3237` n `7`; crypto_alt avg `-0.221` n `223`; crypto_major avg `0.2411` n `7`; equity avg `0.1473` n `47`; fx avg `-0.1569` n `4`; index avg `0.2357` n `6`; metal avg `-0.0569` n `7`; unknown avg `-0.0843` n `313`
- 4h: commodity avg `-1.0832` n `7`; crypto_alt avg `0.0207` n `223`; crypto_major avg `0.7122` n `7`; equity avg `0.7904` n `47`; fx avg `-0.1248` n `4`; index avg `0.943` n `6`; metal avg `0.2632` n `7`; unknown avg `0.1891` n `312`
- 24h: commodity avg `-1.4368` n `7`; crypto_alt avg `1.7498` n `223`; crypto_major avg `2.4267` n `7`; equity avg `1.149` n `47`; fx avg `-0.0583` n `4`; index avg `0.8712` n `6`; metal avg `1.1687` n `7`; unknown avg `0.8728` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.208`, n `368`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2009`, n `368`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `368`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1293`, n `368`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `368`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1058`, n `364`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `368`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1044`, n `368`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.103`, n `368`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0976`, n `364`, weak_sample_signal
