# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T13:45:27.722931+00:00`
- Correlation status: `ready`
- Asset price records: `270`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.643` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1229` n `7`; crypto_alt avg `0.0635` n `223`; crypto_major avg `-0.1161` n `7`; equity avg `-0.0683` n `42`; fx avg `0.0041` n `4`; index avg `0.3831` n `9`; metal avg `0.2643` n `7`; unknown avg `-0.018` n `314`
- 1h: commodity avg `0.4457` n `7`; crypto_alt avg `0.188` n `223`; crypto_major avg `-0.196` n `7`; equity avg `0.0197` n `42`; fx avg `0.0025` n `4`; index avg `0.3189` n `9`; metal avg `-0.0417` n `7`; unknown avg `-0.1934` n `314`
- 4h: commodity avg `0.2433` n `7`; crypto_alt avg `-1.0845` n `223`; crypto_major avg `-1.3924` n `7`; equity avg `-0.3939` n `42`; fx avg `-0.0096` n `4`; index avg `0.2506` n `9`; metal avg `-0.165` n `7`; unknown avg `-0.5538` n `314`
- 24h: commodity avg `0.82` n `7`; crypto_alt avg `1.3444` n `223`; crypto_major avg `0.5493` n `7`; equity avg `0.4421` n `42`; fx avg `-0.0783` n `4`; index avg `0.8703` n `9`; metal avg `-1.2936` n `7`; unknown avg `0.0597` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2673`, n `266`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2593`, n `266`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1812`, n `262`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1703`, n `262`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1667`, n `266`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1651`, n `262`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1641`, n `262`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1627`, n `266`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1612`, n `262`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1579`, n `266`, weak_sample_signal
