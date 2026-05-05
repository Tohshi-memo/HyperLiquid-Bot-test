# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T17:56:58.163246+00:00`
- Correlation status: `ready`
- Asset price records: `379`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0776` n `7`; crypto_alt avg `-0.0308` n `223`; crypto_major avg `-0.0074` n `7`; equity avg `0.026` n `47`; fx avg `-0.0042` n `4`; index avg `-0.0447` n `6`; metal avg `-0.0242` n `7`; unknown avg `-0.0615` n `313`
- 1h: commodity avg `-0.0146` n `7`; crypto_alt avg `0.254` n `223`; crypto_major avg `0.4504` n `7`; equity avg `0.3016` n `47`; fx avg `0.0069` n `4`; index avg `0.1624` n `6`; metal avg `-0.0392` n `7`; unknown avg `-0.0539` n `313`
- 4h: commodity avg `-0.3802` n `7`; crypto_alt avg `-0.2155` n `223`; crypto_major avg `0.0278` n `7`; equity avg `0.4895` n `47`; fx avg `-0.1368` n `4`; index avg `0.3128` n `6`; metal avg `-0.3834` n `7`; unknown avg `-0.3223` n `312`
- 24h: commodity avg `-1.234` n `7`; crypto_alt avg `0.933` n `223`; crypto_major avg `1.4342` n `7`; equity avg `1.4964` n `47`; fx avg `-0.05` n `4`; index avg `1.4125` n `6`; metal avg `0.7516` n `7`; unknown avg `0.681` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2071`, n `375`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2003`, n `375`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.133`, n `375`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1288`, n `375`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1116`, n `371`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1087`, n `375`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1054`, n `375`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `375`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1046`, n `375`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1038`, n `371`, weak_sample_signal
