# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T10:45:26.048663+00:00`
- Correlation status: `ready`
- Asset price records: `258`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4728` n `7`; crypto_alt avg `0.4366` n `223`; crypto_major avg `0.5909` n `7`; equity avg `0.359` n `42`; fx avg `0.0168` n `4`; index avg `0.1568` n `9`; metal avg `0.3147` n `7`; unknown avg `0.2094` n `314`
- 1h: commodity avg `0.4764` n `7`; crypto_alt avg `-1.3068` n `223`; crypto_major avg `-1.1623` n `7`; equity avg `-0.728` n `42`; fx avg `-0.0065` n `4`; index avg `-0.2118` n `9`; metal avg `-0.5386` n `7`; unknown avg `-0.3822` n `314`
- 4h: commodity avg `0.5401` n `7`; crypto_alt avg `-0.7643` n `223`; crypto_major avg `-0.9535` n `7`; equity avg `-0.7644` n `42`; fx avg `-0.0129` n `4`; index avg `-0.5332` n `9`; metal avg `-1.2086` n `7`; unknown avg `-0.0427` n `314`
- 24h: commodity avg `1.0913` n `7`; crypto_alt avg `1.0062` n `223`; crypto_major avg `0.9355` n `7`; equity avg `0.2065` n `42`; fx avg `-0.054` n `4`; index avg `0.3718` n `9`; metal avg `-1.6201` n `7`; unknown avg `-0.0424` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2906`, n `254`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2828`, n `254`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2232`, n `250`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2228`, n `250`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2064`, n `250`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.199`, n `254`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1905`, n `250`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1857`, n `254`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1851`, n `250`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1665`, n `254`, weak_sample_signal
