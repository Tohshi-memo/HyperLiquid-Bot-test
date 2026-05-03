# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T18:15:19.832480+00:00`
- Correlation status: `ready`
- Asset price records: `192`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0589` n `7`; crypto_alt avg `-0.0678` n `223`; crypto_major avg `-0.1052` n `7`; equity avg `-0.0584` n `42`; fx avg `-0.0154` n `4`; index avg `-0.0208` n `9`; metal avg `0.08` n `7`; unknown avg `0.0473` n `314`
- 1h: commodity avg `0.2156` n `7`; crypto_alt avg `0.0309` n `223`; crypto_major avg `-0.0469` n `7`; equity avg `0.0423` n `42`; fx avg `-0.0189` n `4`; index avg `-0.0219` n `9`; metal avg `0.0767` n `7`; unknown avg `-0.0008` n `314`
- 4h: commodity avg `-0.0343` n `7`; crypto_alt avg `-0.0115` n `223`; crypto_major avg `-0.1005` n `7`; equity avg `0.2441` n `42`; fx avg `-0.0183` n `4`; index avg `0.0588` n `9`; metal avg `0.2568` n `7`; unknown avg `0.2399` n `313`
- 24h: commodity avg `-0.1727` n `7`; crypto_alt avg `0.2052` n `223`; crypto_major avg `0.1553` n `7`; equity avg `0.3999` n `42`; fx avg `0.0598` n `4`; index avg `0.0558` n `9`; metal avg `0.4879` n `7`; unknown avg `0.1393` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3993`, n `188`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3856`, n `184`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3814`, n `188`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.379`, n `184`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3768`, n `188`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3634`, n `188`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3269`, n `188`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3079`, n `188`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3044`, n `188`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2655`, n `184`, moderate_sample_signal
