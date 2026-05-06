# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T02:45:17.770039+00:00`
- Correlation status: `ready`
- Asset price records: `415`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7206` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0363` n `7`; crypto_alt avg `0.1012` n `223`; crypto_major avg `0.0238` n `7`; equity avg `-0.0394` n `47`; fx avg `0.011` n `4`; index avg `-0.0329` n `6`; metal avg `0.1357` n `7`; unknown avg `0.1137` n `313`
- 1h: commodity avg `0.0999` n `7`; crypto_alt avg `-0.0036` n `223`; crypto_major avg `-0.1417` n `7`; equity avg `0.0087` n `47`; fx avg `0.0435` n `4`; index avg `-0.0831` n `6`; metal avg `0.1562` n `7`; unknown avg `0.0095` n `313`
- 4h: commodity avg `-0.5262` n `7`; crypto_alt avg `0.9011` n `223`; crypto_major avg `-0.0151` n `7`; equity avg `0.2788` n `47`; fx avg `-0.2531` n `4`; index avg `0.5246` n `6`; metal avg `1.7055` n `7`; unknown avg `-0.2991` n `313`
- 24h: commodity avg `-1.3648` n `7`; crypto_alt avg `2.086` n `223`; crypto_major avg `1.4729` n `7`; equity avg `2.5615` n `47`; fx avg `-0.177` n `4`; index avg `2.1494` n `6`; metal avg `1.6087` n `7`; unknown avg `1.2781` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1849`, n `411`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1786`, n `411`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1283`, n `411`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `411`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1187`, n `411`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1043`, n `411`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1008`, n `407`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0968`, n `411`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.096`, n `411`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0949`, n `407`, weak_sample_signal
