# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T14:45:28.900936+00:00`
- Correlation status: `ready`
- Asset price records: `274`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.167` n `7`; crypto_alt avg `0.1572` n `223`; crypto_major avg `0.3561` n `7`; equity avg `0.3315` n `42`; fx avg `-0.0117` n `4`; index avg `0.1305` n `9`; metal avg `0.058` n `7`; unknown avg `-0.0994` n `314`
- 1h: commodity avg `0.0715` n `7`; crypto_alt avg `0.3649` n `223`; crypto_major avg `0.7666` n `7`; equity avg `0.847` n `42`; fx avg `-0.0019` n `4`; index avg `0.2424` n `9`; metal avg `0.2804` n `7`; unknown avg `-0.3062` n `314`
- 4h: commodity avg `-0.1526` n `7`; crypto_alt avg `0.5599` n `223`; crypto_major avg `0.5325` n `7`; equity avg `1.1844` n `42`; fx avg `-0.005` n `4`; index avg `0.7103` n `9`; metal avg `0.6581` n `7`; unknown avg `-0.3832` n `314`
- 24h: commodity avg `0.9192` n `7`; crypto_alt avg `1.5948` n `223`; crypto_major avg `1.1621` n `7`; equity avg `1.2602` n `42`; fx avg `-0.0728` n `4`; index avg `1.1212` n `9`; metal avg `-1.0584` n `7`; unknown avg `-0.2452` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.259`, n `270`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2503`, n `270`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2426`, n `266`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2396`, n `266`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1579`, n `270`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.152`, n `270`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1508`, n `270`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1495`, n `270`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1475`, n `266`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1384`, n `266`, weak_sample_signal
