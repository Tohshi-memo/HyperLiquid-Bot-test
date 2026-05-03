# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T05:45:38.913444+00:00`
- Correlation status: `ready`
- Asset price records: `142`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `7`; crypto_alt avg `-0.0961` n `223`; crypto_major avg `-0.0494` n `7`; equity avg `0.0517` n `42`; fx avg `0.004` n `4`; index avg `0.0257` n `9`; metal avg `-0.0073` n `7`; unknown avg `-0.0132` n `313`
- 1h: commodity avg `-0.0209` n `7`; crypto_alt avg `-0.0967` n `223`; crypto_major avg `0.0187` n `7`; equity avg `-0.0249` n `42`; fx avg `0.0074` n `4`; index avg `-0.0164` n `9`; metal avg `0.0066` n `7`; unknown avg `0.3092` n `313`
- 4h: commodity avg `0.0053` n `7`; crypto_alt avg `-0.1202` n `223`; crypto_major avg `0.0061` n `7`; equity avg `-0.0776` n `42`; fx avg `0.0082` n `4`; index avg `-0.0343` n `9`; metal avg `0.0314` n `7`; unknown avg `0.3454` n `313`
- 24h: commodity avg `-0.1238` n `7`; crypto_alt avg `1.1663` n `223`; crypto_major avg `-0.0195` n `7`; equity avg `0.5248` n `42`; fx avg `0.1499` n `4`; index avg `0.0168` n `9`; metal avg `0.0829` n `7`; unknown avg `0.4009` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4429`, n `138`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4277`, n `138`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4087`, n `134`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4066`, n `134`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4043`, n `138`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.395`, n `134`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3904`, n `134`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3865`, n `138`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3591`, n `134`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3539`, n `138`, moderate_sample_signal
