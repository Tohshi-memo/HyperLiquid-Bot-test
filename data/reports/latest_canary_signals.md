# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T01:30:22.103953+00:00`
- Correlation status: `ready`
- Asset price records: `29`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.037` n `7`; crypto_alt avg `0.0551` n `223`; crypto_major avg `-0.0305` n `7`; equity avg `0.1157` n `42`; fx avg `0.0` n `4`; index avg `0.0016` n `9`; metal avg `0.002` n `7`; unknown avg `-0.0078` n `311`
- 1h: commodity avg `-0.0333` n `7`; crypto_alt avg `0.335` n `223`; crypto_major avg `0.1264` n `7`; equity avg `0.0973` n `42`; fx avg `0.0` n `4`; index avg `0.0272` n `9`; metal avg `-0.0113` n `7`; unknown avg `0.0481` n `311`
- 4h: commodity avg `0.1865` n `7`; crypto_alt avg `-0.1138` n `223`; crypto_major avg `-0.1364` n `7`; equity avg `0.4346` n `42`; fx avg `0.0254` n `4`; index avg `0.0341` n `9`; metal avg `-0.124` n `7`; unknown avg `0.0294` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6761`, n `25`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6517`, n `25`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5581`, n `25`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5397`, n `25`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.508`, n `25`, strong_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.4908`, n `25`, moderate_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.4848`, n `25`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3736`, n `25`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3542`, n `25`, moderate_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2855`, n `25`, moderate_sample_signal
