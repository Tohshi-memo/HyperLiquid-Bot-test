# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T14:00:30.120729+00:00`
- Correlation status: `ready`
- Asset price records: `271`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6236` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1243` n `7`; crypto_alt avg `-0.0459` n `223`; crypto_major avg `-0.0058` n `7`; equity avg `0.4527` n `42`; fx avg `0.0026` n `4`; index avg `-0.0355` n `9`; metal avg `0.1181` n `7`; unknown avg `-0.3196` n `314`
- 1h: commodity avg `-0.1419` n `7`; crypto_alt avg `0.3826` n `223`; crypto_major avg `0.2425` n `7`; equity avg `0.711` n `42`; fx avg `0.0004` n `4`; index avg `0.431` n `9`; metal avg `0.2857` n `7`; unknown avg `-0.4295` n `314`
- 4h: commodity avg `0.0871` n `7`; crypto_alt avg `-1.1613` n `223`; crypto_major avg `-1.387` n `7`; equity avg `0.1086` n `42`; fx avg `-0.0046` n `4`; index avg `0.2366` n `9`; metal avg `0.0226` n `7`; unknown avg `-0.8764` n `314`
- 24h: commodity avg `0.7443` n `7`; crypto_alt avg `1.2601` n `223`; crypto_major avg `0.4847` n `7`; equity avg `0.909` n `42`; fx avg `-0.0757` n `4`; index avg `0.8385` n `9`; metal avg `-1.1809` n `7`; unknown avg `-0.2933` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2658`, n `267`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2576`, n `267`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1784`, n `263`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1779`, n `263`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1655`, n `263`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1622`, n `267`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1614`, n `267`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1605`, n `263`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1557`, n `267`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1549`, n `267`, weak_sample_signal
