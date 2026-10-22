# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T05:22:33.229140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.91` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.3763` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0328` n `13`; crypto_alt avg `-0.1392` n `237`; crypto_major avg `-0.0741` n `8`; equity avg `-0.1797` n `151`; fx avg `-0.0043` n `6`; index avg `-0.0374` n `26`; metal avg `-0.0369` n `20`; unknown avg `-0.4166` n `1201`
- 1h: commodity avg `0.1218` n `13`; crypto_alt avg `-0.4176` n `237`; crypto_major avg `-0.1891` n `8`; equity avg `-0.1151` n `151`; fx avg `-0.0034` n `6`; index avg `-0.0576` n `26`; metal avg `-0.0314` n `20`; unknown avg `-0.5402` n `1199`
- 4h: commodity avg `0.2345` n `13`; crypto_alt avg `-2.3102` n `237`; crypto_major avg `-1.6313` n `8`; equity avg `-1.4557` n `151`; fx avg `-0.0561` n `6`; index avg `-0.255` n `26`; metal avg `-0.3087` n `20`; unknown avg `4.1406` n `1177`
- 24h: commodity avg `-0.3719` n `13`; crypto_alt avg `-0.845` n `237`; crypto_major avg `-0.6983` n `8`; equity avg `-2.2458` n `151`; fx avg `0.0062` n `6`; index avg `-0.3736` n `26`; metal avg `-0.5911` n `20`; unknown avg `118.964` n `930`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
