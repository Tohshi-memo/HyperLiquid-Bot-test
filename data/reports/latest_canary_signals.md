# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T09:59:27.019115+00:00`
- Correlation status: `ready`
- Asset price records: `254`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0696` n `7`; crypto_alt avg `0.4435` n `223`; crypto_major avg `0.2843` n `7`; equity avg `-0.063` n `42`; fx avg `-0.0045` n `4`; index avg `0.0089` n `9`; metal avg `-0.1427` n `7`; unknown avg `0.206` n `314`
- 1h: commodity avg `-0.0915` n `7`; crypto_alt avg `0.6115` n `223`; crypto_major avg `0.2751` n `7`; equity avg `0.0349` n `42`; fx avg `0.0061` n `4`; index avg `-0.1315` n `9`; metal avg `-0.1075` n `7`; unknown avg `0.1933` n `314`
- 4h: commodity avg `0.557` n `7`; crypto_alt avg `0.1547` n `223`; crypto_major avg `-0.4382` n `7`; equity avg `-0.1899` n `42`; fx avg `0.014` n `4`; index avg `-0.2824` n `9`; metal avg `-1.0263` n `7`; unknown avg `0.0311` n `312`
- 24h: commodity avg `0.4953` n `7`; crypto_alt avg `2.3718` n `223`; crypto_major avg `2.0023` n `7`; equity avg `0.9927` n `42`; fx avg `-0.0428` n `4`; index avg `0.616` n `9`; metal avg `-1.0785` n `7`; unknown avg `0.3191` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3351`, n `250`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3243`, n `250`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2489`, n `246`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2462`, n `246`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2175`, n `246`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.205`, n `246`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1945`, n `250`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1806`, n `246`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1778`, n `250`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1717`, n `250`, weak_sample_signal
