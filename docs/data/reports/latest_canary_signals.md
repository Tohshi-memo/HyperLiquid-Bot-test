# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T14:30:38.638339+00:00`
- Correlation status: `ready`
- Asset price records: `368`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0303` n `7`; crypto_alt avg `0.0288` n `223`; crypto_major avg `0.062` n `7`; equity avg `-0.0193` n `47`; fx avg `-0.0011` n `4`; index avg `0.0026` n `6`; metal avg `-0.0939` n `7`; unknown avg `0.0061` n `313`
- 1h: commodity avg `-0.2686` n `7`; crypto_alt avg `-0.1389` n `223`; crypto_major avg `-0.1154` n `7`; equity avg `0.7094` n `47`; fx avg `0.0134` n `4`; index avg `0.2723` n `6`; metal avg `0.0314` n `7`; unknown avg `0.1345` n `312`
- 4h: commodity avg `-0.6292` n `7`; crypto_alt avg `0.2444` n `223`; crypto_major avg `0.8125` n `7`; equity avg `0.7861` n `47`; fx avg `0.0443` n `4`; index avg `0.6048` n `6`; metal avg `0.3787` n `7`; unknown avg `0.5222` n `312`
- 24h: commodity avg `-0.1464` n `7`; crypto_alt avg `2.0489` n `223`; crypto_major avg `2.1492` n `7`; equity avg `0.724` n `47`; fx avg `0.0805` n `4`; index avg `0.5831` n `6`; metal avg `0.3154` n `7`; unknown avg `0.387` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.208`, n `364`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2008`, n `364`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1341`, n `364`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.13`, n `364`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `364`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1046`, n `364`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `364`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1018`, n `364`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0956`, n `360`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0949`, n `360`, weak_sample_signal
