# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T15:30:26.662326+00:00`
- Correlation status: `ready`
- Asset price records: `277`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.4625` n `7`; crypto_alt avg `-0.5208` n `223`; crypto_major avg `-0.7007` n `7`; equity avg `-0.665` n `42`; fx avg `-0.0086` n `4`; index avg `-0.2509` n `9`; metal avg `-0.4292` n `7`; unknown avg `-0.2603` n `314`
- 1h: commodity avg `1.0028` n `7`; crypto_alt avg `0.0455` n `223`; crypto_major avg `-0.0312` n `7`; equity avg `-0.4054` n `42`; fx avg `-0.0182` n `4`; index avg `-0.1508` n `9`; metal avg `-0.8985` n `7`; unknown avg `-0.3676` n `314`
- 4h: commodity avg `0.6649` n `7`; crypto_alt avg `0.6635` n `223`; crypto_major avg `0.3913` n `7`; equity avg `0.2421` n `42`; fx avg `0.001` n `4`; index avg `0.3819` n `9`; metal avg `-0.2152` n `7`; unknown avg `-0.493` n `314`
- 24h: commodity avg `1.9748` n `7`; crypto_alt avg `1.3235` n `223`; crypto_major avg `0.7711` n `7`; equity avg `0.5512` n `42`; fx avg `-0.0828` n `4`; index avg `0.7976` n `9`; metal avg `-2.0216` n `7`; unknown avg `-0.7222` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2519`, n `273`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2454`, n `269`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2445`, n `273`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2424`, n `269`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1533`, n `273`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1513`, n `273`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1461`, n `273`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1436`, n `269`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1415`, n `273`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.136`, n `269`, weak_sample_signal
