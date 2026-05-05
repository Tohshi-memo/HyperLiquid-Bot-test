# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T06:15:44.202565+00:00`
- Correlation status: `ready`
- Asset price records: `335`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1552` n `7`; crypto_alt avg `-0.0172` n `223`; crypto_major avg `-0.1194` n `7`; equity avg `0.0084` n `47`; fx avg `0.0067` n `4`; index avg `0.0062` n `6`; metal avg `-0.2153` n `7`; unknown avg `0.0229` n `312`
- 1h: commodity avg `0.1337` n `7`; crypto_alt avg `0.0159` n `223`; crypto_major avg `0.1178` n `7`; equity avg `0.2539` n `47`; fx avg `0.0123` n `4`; index avg `0.0471` n `6`; metal avg `0.0381` n `7`; unknown avg `1.9319` n `310`
- 4h: commodity avg `0.1215` n `7`; crypto_alt avg `0.2003` n `223`; crypto_major avg `0.5111` n `7`; equity avg `0.6964` n `47`; fx avg `0.0063` n `4`; index avg `0.2896` n `6`; metal avg `0.1004` n `7`; unknown avg `1.4619` n `310`
- 24h: commodity avg `1.414` n `7`; crypto_alt avg `0.832` n `223`; crypto_major avg `0.2053` n `7`; equity avg `-0.2916` n `47`; fx avg `-0.0273` n `4`; index avg `-0.1145` n `6`; metal avg `-1.3227` n `7`; unknown avg `0.5382` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2222`, n `331`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2155`, n `331`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1395`, n `331`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.135`, n `331`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1332`, n `331`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1139`, n `331`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1078`, n `331`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.107`, n `331`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1037`, n `327`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1035`, n `327`, weak_sample_signal
