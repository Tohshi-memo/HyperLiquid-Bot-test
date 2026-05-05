# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T20:30:28.025836+00:00`
- Correlation status: `ready`
- Asset price records: `390`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0314` n `7`; crypto_alt avg `0.1941` n `223`; crypto_major avg `0.0796` n `7`; equity avg `0.4732` n `47`; fx avg `0.0234` n `4`; index avg `0.09` n `6`; metal avg `0.0734` n `7`; unknown avg `0.069` n `313`
- 1h: commodity avg `-0.0179` n `7`; crypto_alt avg `0.3964` n `223`; crypto_major avg `0.19` n `7`; equity avg `0.4618` n `47`; fx avg `0.0202` n `4`; index avg `0.049` n `6`; metal avg `-0.0017` n `7`; unknown avg `-0.2032` n `313`
- 4h: commodity avg `-0.1151` n `7`; crypto_alt avg `0.8476` n `223`; crypto_major avg `0.6482` n `7`; equity avg `0.586` n `47`; fx avg `0.0421` n `4`; index avg `0.2267` n `6`; metal avg `-0.1266` n `7`; unknown avg `0.0199` n `313`
- 24h: commodity avg `-1.1255` n `7`; crypto_alt avg `2.3893` n `223`; crypto_major avg `2.6835` n `7`; equity avg `2.4168` n `47`; fx avg `-0.0178` n `4`; index avg `1.4477` n `6`; metal avg `0.7786` n `7`; unknown avg `1.121` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2069`, n `386`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2`, n `386`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1311`, n `386`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1271`, n `386`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1138`, n `382`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `386`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1072`, n `386`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1061`, n `382`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1036`, n `386`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1028`, n `386`, weak_sample_signal
