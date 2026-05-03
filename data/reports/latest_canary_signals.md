# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T22:45:19.102296+00:00`
- Correlation status: `ready`
- Asset price records: `210`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0282` n `7`; crypto_alt avg `0.1251` n `223`; crypto_major avg `0.2478` n `7`; equity avg `0.0588` n `42`; fx avg `-0.005` n `4`; index avg `0.0411` n `9`; metal avg `0.1894` n `7`; unknown avg `-0.0594` n `314`
- 1h: commodity avg `0.3602` n `7`; crypto_alt avg `0.8327` n `223`; crypto_major avg `1.0321` n `7`; equity avg `0.0837` n `42`; fx avg `-0.0064` n `4`; index avg `-0.0759` n `9`; metal avg `-0.0172` n `7`; unknown avg `0.3058` n `314`
- 4h: commodity avg `-0.1672` n `7`; crypto_alt avg `0.4775` n `223`; crypto_major avg `0.7777` n `7`; equity avg `0.2137` n `42`; fx avg `-0.0172` n `4`; index avg `0.0079` n `9`; metal avg `0.0766` n `7`; unknown avg `0.2019` n `314`
- 24h: commodity avg `-0.2814` n `7`; crypto_alt avg `0.1351` n `223`; crypto_major avg `0.6848` n `7`; equity avg `0.3966` n `42`; fx avg `-0.0126` n `4`; index avg `0.0606` n `9`; metal avg `0.5596` n `7`; unknown avg `0.2143` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3919`, n `206`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3747`, n `206`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3572`, n `202`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3542`, n `202`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3235`, n `206`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3126`, n `206`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3101`, n `206`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2934`, n `206`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.2913`, n `206`, moderate_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.2309`, n `206`, weak_sample_signal
