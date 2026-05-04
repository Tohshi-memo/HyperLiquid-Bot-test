# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T00:15:18.739987+00:00`
- Correlation status: `ready`
- Asset price records: `216`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.048` n `7`; crypto_alt avg `-0.2093` n `223`; crypto_major avg `-0.0792` n `7`; equity avg `0.0438` n `42`; fx avg `-0.0064` n `4`; index avg `-0.0437` n `9`; metal avg `-0.0251` n `7`; unknown avg `0.0139` n `314`
- 1h: commodity avg `0.2678` n `7`; crypto_alt avg `-0.6959` n `223`; crypto_major avg `-0.7472` n `7`; equity avg `-0.0394` n `42`; fx avg `-0.0011` n `4`; index avg `0.1056` n `9`; metal avg `-0.04` n `7`; unknown avg `0.358` n `314`
- 4h: commodity avg `0.2533` n `7`; crypto_alt avg `-0.8349` n `223`; crypto_major avg `-0.4556` n `7`; equity avg `-0.091` n `42`; fx avg `-0.0739` n `4`; index avg `0.0572` n `9`; metal avg `-0.0672` n `7`; unknown avg `0.0982` n `314`
- 24h: commodity avg `0.1417` n `7`; crypto_alt avg `-0.461` n `223`; crypto_major avg `0.0714` n `7`; equity avg `0.0648` n `42`; fx avg `-0.0233` n `4`; index avg `0.1379` n `9`; metal avg `0.3481` n `7`; unknown avg `0.0294` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3902`, n `212`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3733`, n `212`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2971`, n `208`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2963`, n `208`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2918`, n `212`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2812`, n `212`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2792`, n `208`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2741`, n `208`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2366`, n `212`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.2273`, n `212`, weak_sample_signal
