# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T16:07:27.604945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `0.0133` n `234`; crypto_major avg `-0.051` n `8`; equity avg `0.0129` n `141`; fx avg `0.002` n `6`; index avg `0.0002` n `26`; metal avg `0.0014` n `20`; unknown avg `-0.0342` n `945`
- 1h: commodity avg `-0.0323` n `12`; crypto_alt avg `0.4498` n `234`; crypto_major avg `0.237` n `8`; equity avg `0.0217` n `141`; fx avg `-0.0025` n `6`; index avg `-0.0` n `26`; metal avg `-0.0065` n `20`; unknown avg `0.8698` n `945`
- 4h: commodity avg `0.0177` n `12`; crypto_alt avg `0.9897` n `234`; crypto_major avg `0.2412` n `8`; equity avg `0.0954` n `141`; fx avg `-0.0065` n `6`; index avg `0.0125` n `26`; metal avg `-0.0093` n `20`; unknown avg `3.0743` n `945`
- 24h: commodity avg `0.4317` n `12`; crypto_alt avg `3.3199` n `234`; crypto_major avg `0.1136` n `8`; equity avg `-0.2583` n `141`; fx avg `0.0264` n `6`; index avg `-0.0368` n `26`; metal avg `-0.0905` n `20`; unknown avg `-0.4248` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
