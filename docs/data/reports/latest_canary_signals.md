# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T19:15:41.497461+00:00`
- Correlation status: `ready`
- Asset price records: `385`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `7`; crypto_alt avg `-0.0382` n `223`; crypto_major avg `-0.0847` n `7`; equity avg `-0.0761` n `47`; fx avg `0.0135` n `4`; index avg `0.006` n `6`; metal avg `-0.0695` n `7`; unknown avg `0.0096` n `313`
- 1h: commodity avg `-0.0478` n `7`; crypto_alt avg `0.065` n `223`; crypto_major avg `-0.1633` n `7`; equity avg `-0.0447` n `47`; fx avg `0.0093` n `4`; index avg `0.0154` n `6`; metal avg `-0.1743` n `7`; unknown avg `-0.0522` n `313`
- 4h: commodity avg `0.0236` n `7`; crypto_alt avg `0.1504` n `223`; crypto_major avg `0.0323` n `7`; equity avg `0.0976` n `47`; fx avg `0.0037` n `4`; index avg `0.2865` n `6`; metal avg `-0.5451` n `7`; unknown avg `1.0992` n `313`
- 24h: commodity avg `-1.2234` n `7`; crypto_alt avg `1.396` n `223`; crypto_major avg `1.9991` n `7`; equity avg `1.6397` n `47`; fx avg `-0.0252` n `4`; index avg `1.4815` n `6`; metal avg `0.6814` n `7`; unknown avg `2.6162` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2069`, n `381`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2002`, n `381`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1317`, n `381`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1276`, n `381`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.114`, n `377`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.109`, n `381`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1063`, n `377`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `381`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1048`, n `381`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `381`, weak_sample_signal
