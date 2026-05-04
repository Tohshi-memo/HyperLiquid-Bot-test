# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T08:45:43.078853+00:00`
- Correlation status: `ready`
- Asset price records: `250`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1005` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0831` n `7`; crypto_alt avg `-0.0908` n `223`; crypto_major avg `0.0164` n `7`; equity avg `0.004` n `42`; fx avg `0.0122` n `4`; index avg `-0.051` n `9`; metal avg `0.0533` n `7`; unknown avg `0.0031` n `314`
- 1h: commodity avg `0.106` n `7`; crypto_alt avg `-0.1813` n `223`; crypto_major avg `-0.2016` n `7`; equity avg `-0.2071` n `42`; fx avg `0.0138` n `4`; index avg `-0.095` n `9`; metal avg `-0.2093` n `7`; unknown avg `0.3333` n `314`
- 4h: commodity avg `0.4519` n `7`; crypto_alt avg `-0.6329` n `223`; crypto_major avg `-1.168` n `7`; equity avg `-0.3988` n `42`; fx avg `0.0247` n `4`; index avg `-0.0675` n `9`; metal avg `-1.1327` n `7`; unknown avg `-0.1616` n `312`
- 24h: commodity avg `0.5636` n `7`; crypto_alt avg `1.8551` n `223`; crypto_major avg `1.9644` n `7`; equity avg `1.0424` n `42`; fx avg `-0.0483` n `4`; index avg `0.7203` n `9`; metal avg `-0.9475` n `7`; unknown avg `0.1465` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3358`, n `246`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.325`, n `246`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3184`, n `242`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.313`, n `242`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2167`, n `242`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.2044`, n `242`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1956`, n `246`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1794`, n `242`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.178`, n `246`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.172`, n `246`, weak_sample_signal
