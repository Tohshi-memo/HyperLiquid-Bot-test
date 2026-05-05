# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T17:45:52.801346+00:00`
- Correlation status: `ready`
- Asset price records: `379`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `7`; crypto_alt avg `-0.0402` n `223`; crypto_major avg `-0.0636` n `7`; equity avg `0.0119` n `47`; fx avg `-0.0013` n `4`; index avg `-0.0626` n `6`; metal avg `0.0303` n `7`; unknown avg `0.0394` n `313`
- 1h: commodity avg `-0.1` n `7`; crypto_alt avg `0.2437` n `223`; crypto_major avg `0.3944` n `7`; equity avg `0.287` n `47`; fx avg `0.0099` n `4`; index avg `0.1445` n `6`; metal avg `0.0154` n `7`; unknown avg `0.0498` n `313`
- 4h: commodity avg `-0.4651` n `7`; crypto_alt avg `-0.2265` n `223`; crypto_major avg `-0.0279` n `7`; equity avg `0.4759` n `47`; fx avg `-0.1339` n `4`; index avg `0.2948` n `6`; metal avg `-0.3291` n `7`; unknown avg `-0.2199` n `312`
- 24h: commodity avg `-1.3169` n `7`; crypto_alt avg `0.9206` n `223`; crypto_major avg `1.3775` n `7`; equity avg `1.482` n `47`; fx avg `-0.0471` n `4`; index avg `1.3943` n `6`; metal avg `0.8065` n `7`; unknown avg `0.7867` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.207`, n `375`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2002`, n `375`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1331`, n `375`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1289`, n `375`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1114`, n `371`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1084`, n `375`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1054`, n `375`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `375`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1046`, n `375`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1035`, n `371`, weak_sample_signal
