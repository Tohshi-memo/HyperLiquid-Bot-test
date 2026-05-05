# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T02:15:29.506953+00:00`
- Correlation status: `ready`
- Asset price records: `319`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0508` n `7`; crypto_alt avg `0.1018` n `223`; crypto_major avg `0.2011` n `7`; equity avg `0.0869` n `47`; fx avg `-0.0021` n `4`; index avg `0.0031` n `6`; metal avg `0.0769` n `7`; unknown avg `-0.0046` n `312`
- 1h: commodity avg `-0.1799` n `7`; crypto_alt avg `0.2788` n `223`; crypto_major avg `0.2529` n `7`; equity avg `-0.0377` n `47`; fx avg `-0.0034` n `4`; index avg `0.0275` n `6`; metal avg `0.0911` n `7`; unknown avg `0.1787` n `312`
- 4h: commodity avg `-0.1888` n `7`; crypto_alt avg `0.3473` n `223`; crypto_major avg `0.2452` n `7`; equity avg `0.069` n `47`; fx avg `-0.0117` n `4`; index avg `0.0488` n `6`; metal avg `0.4498` n `7`; unknown avg `-0.0436` n `312`
- 24h: commodity avg `1.1541` n `7`; crypto_alt avg `1.4242` n `223`; crypto_major avg `0.0547` n `7`; equity avg `-0.8123` n `47`; fx avg `-0.0667` n `4`; index avg `-0.1817` n `6`; metal avg `-1.7337` n `7`; unknown avg `-1.5099` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2305`, n `315`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2241`, n `315`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1566`, n `311`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1545`, n `311`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.153`, n `315`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1439`, n `315`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1388`, n `315`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1298`, n `315`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1234`, n `311`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.123`, n `315`, weak_sample_signal
