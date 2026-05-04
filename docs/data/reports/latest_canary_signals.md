# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T02:30:23.896968+00:00`
- Correlation status: `ready`
- Asset price records: `225`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1382` n `7`; crypto_alt avg `0.3076` n `223`; crypto_major avg `0.0835` n `7`; equity avg `-0.0266` n `42`; fx avg `0.0013` n `4`; index avg `0.0083` n `9`; metal avg `-0.2624` n `7`; unknown avg `-0.3036` n `314`
- 1h: commodity avg `0.0846` n `7`; crypto_alt avg `1.3436` n `223`; crypto_major avg `1.3589` n `7`; equity avg `0.5202` n `42`; fx avg `0.0279` n `4`; index avg `0.2081` n `9`; metal avg `0.1125` n `7`; unknown avg `-0.1515` n `314`
- 4h: commodity avg `0.4571` n `7`; crypto_alt avg `0.9134` n `223`; crypto_major avg `1.0666` n `7`; equity avg `0.5753` n `42`; fx avg `0.0263` n `4`; index avg `0.5027` n `9`; metal avg `-0.3768` n `7`; unknown avg `-0.1689` n `314`
- 24h: commodity avg `0.1802` n `7`; crypto_alt avg `2.3168` n `223`; crypto_major avg `2.4175` n `7`; equity avg `0.9468` n `42`; fx avg `0.0122` n `4`; index avg `0.5461` n `9`; metal avg `-0.0063` n `7`; unknown avg `0.3918` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.376`, n `221`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3642`, n `217`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3604`, n `221`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3589`, n `217`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2093`, n `221`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2026`, n `221`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1995`, n `221`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1851`, n `217`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1755`, n `217`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1531`, n `221`, weak_sample_signal
