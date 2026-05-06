# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T03:00:30.438004+00:00`
- Correlation status: `ready`
- Asset price records: `416`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0157` n `7`; crypto_alt avg `0.381` n `223`; crypto_major avg `0.3598` n `7`; equity avg `0.1429` n `47`; fx avg `-0.0184` n `4`; index avg `0.0144` n `6`; metal avg `0.2277` n `7`; unknown avg `0.0412` n `313`
- 1h: commodity avg `0.0277` n `7`; crypto_alt avg `0.0597` n `223`; crypto_major avg `0.068` n `7`; equity avg `0.0657` n `47`; fx avg `0.029` n `4`; index avg `-0.1053` n `6`; metal avg `0.3063` n `7`; unknown avg `0.1164` n `313`
- 4h: commodity avg `-0.099` n `7`; crypto_alt avg `1.1027` n `223`; crypto_major avg `0.1573` n `7`; equity avg `0.0861` n `47`; fx avg `-0.2687` n `4`; index avg `0.3497` n `6`; metal avg `1.3845` n `7`; unknown avg `-0.2374` n `313`
- 24h: commodity avg `-1.4013` n `7`; crypto_alt avg `2.7015` n `223`; crypto_major avg `2.1698` n `7`; equity avg `2.6805` n `47`; fx avg `-0.1879` n `4`; index avg `2.18` n `6`; metal avg `1.9434` n `7`; unknown avg `1.4513` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1843`, n `412`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1781`, n `412`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1283`, n `412`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `412`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1202`, n `412`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `412`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1003`, n `408`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0968`, n `412`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.096`, n `412`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0942`, n `408`, weak_sample_signal
