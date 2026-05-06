# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T07:30:29.688495+00:00`
- Correlation status: `ready`
- Asset price records: `434`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0907` n `7`; crypto_alt avg `0.1393` n `223`; crypto_major avg `0.1543` n `7`; equity avg `-0.0342` n `47`; fx avg `-0.0167` n `4`; index avg `-0.0048` n `6`; metal avg `0.0963` n `7`; unknown avg `1.1006` n `313`
- 1h: commodity avg `0.0078` n `7`; crypto_alt avg `0.6562` n `223`; crypto_major avg `0.4809` n `7`; equity avg `-0.0154` n `47`; fx avg `0.0474` n `4`; index avg `-0.14` n `6`; metal avg `-0.1045` n `7`; unknown avg `1.4042` n `313`
- 4h: commodity avg `-0.081` n `7`; crypto_alt avg `0.5995` n `223`; crypto_major avg `0.3644` n `7`; equity avg `0.3755` n `47`; fx avg `-0.2043` n `4`; index avg `0.1922` n `6`; metal avg `0.1613` n `7`; unknown avg `1.9082` n `311`
- 24h: commodity avg `-1.4753` n `7`; crypto_alt avg `2.7838` n `223`; crypto_major avg `1.9189` n `7`; equity avg `2.3678` n `47`; fx avg `-0.3489` n `4`; index avg `2.1526` n `6`; metal avg `1.9002` n `7`; unknown avg `2.0819` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1806`, n `430`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1743`, n `430`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1253`, n `430`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1251`, n `430`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1213`, n `430`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1079`, n `430`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0995`, n `426`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0943`, n `426`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0935`, n `430`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0928`, n `430`, weak_sample_signal
