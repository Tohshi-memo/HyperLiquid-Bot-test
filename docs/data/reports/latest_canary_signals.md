# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T15:15:56.963090+00:00`
- Correlation status: `ready`
- Asset price records: `369`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.288` n `7`; crypto_alt avg `-0.1364` n `223`; crypto_major avg `0.1755` n `7`; equity avg `-0.0062` n `47`; fx avg `-0.1444` n `4`; index avg `0.155` n `6`; metal avg `-0.1048` n `7`; unknown avg `-0.07` n `313`
- 1h: commodity avg `-0.258` n `7`; crypto_alt avg `-0.1075` n `223`; crypto_major avg `0.2376` n `7`; equity avg `-0.0253` n `47`; fx avg `-0.1455` n `4`; index avg `0.1576` n `6`; metal avg `-0.1985` n `7`; unknown avg `-0.0621` n `313`
- 4h: commodity avg `-1.1646` n `7`; crypto_alt avg `0.2561` n `223`; crypto_major avg `0.6764` n `7`; equity avg `0.6227` n `47`; fx avg `-0.1039` n `4`; index avg `0.8669` n `6`; metal avg `0.309` n `7`; unknown avg `0.3089` n `312`
- 24h: commodity avg `-0.9549` n `7`; crypto_alt avg `1.3002` n `223`; crypto_major avg `1.6458` n `7`; equity avg `0.3575` n `47`; fx avg `-0.0544` n `4`; index avg `0.6151` n `6`; metal avg `0.6849` n `7`; unknown avg `0.5244` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.208`, n `367`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2008`, n `367`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1335`, n `367`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1295`, n `367`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1055`, n `367`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.105`, n `367`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `367`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1029`, n `367`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1026`, n `363`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0945`, n `363`, weak_sample_signal
