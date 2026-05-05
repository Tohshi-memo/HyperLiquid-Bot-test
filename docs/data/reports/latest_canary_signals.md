# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T00:15:17.383067+00:00`
- Correlation status: `ready`
- Asset price records: `311`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0532` n `7`; crypto_alt avg `0.0656` n `223`; crypto_major avg `0.1394` n `7`; equity avg `0.1924` n `47`; fx avg `-0.0029` n `4`; index avg `0.0183` n `6`; metal avg `0.0878` n `7`; unknown avg `-0.057` n `312`
- 1h: commodity avg `-0.0667` n `7`; crypto_alt avg `0.0964` n `223`; crypto_major avg `-0.03` n `7`; equity avg `0.1974` n `47`; fx avg `-0.0042` n `4`; index avg `0.0058` n `6`; metal avg `0.0909` n `7`; unknown avg `-0.0911` n `312`
- 4h: commodity avg `-0.0439` n `7`; crypto_alt avg `-0.0889` n `223`; crypto_major avg `-0.1234` n `7`; equity avg `0.009` n `47`; fx avg `-0.0019` n `4`; index avg `-0.1644` n `6`; metal avg `0.125` n `7`; unknown avg `-0.1785` n `312`
- 24h: commodity avg `1.1826` n `7`; crypto_alt avg `2.2313` n `223`; crypto_major avg `1.1579` n `7`; equity avg `-0.3512` n `47`; fx avg `-0.0204` n `4`; index avg `-0.1255` n `6`; metal avg `-2.2326` n `7`; unknown avg `-1.2554` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2355`, n `307`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2297`, n `307`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1849`, n `303`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1826`, n `303`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1498`, n `307`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1474`, n `307`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1419`, n `307`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1303`, n `307`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1202`, n `303`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1201`, n `307`, weak_sample_signal
