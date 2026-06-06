# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T10:52:21.206026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1257` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0093` n `12`; crypto_alt avg `0.3108` n `228`; crypto_major avg `0.1758` n `8`; equity avg `0.0235` n `74`; fx avg `0.0` n `6`; index avg `-0.0043` n `23`; metal avg `-0.0081` n `18`; unknown avg `0.0065` n `425`
- 1h: commodity avg `-0.0146` n `12`; crypto_alt avg `-1.1395` n `228`; crypto_major avg `-1.1343` n `8`; equity avg `-0.2928` n `74`; fx avg `0.0005` n `6`; index avg `-0.0086` n `23`; metal avg `-0.1182` n `18`; unknown avg `-0.0781` n `425`
- 4h: commodity avg `0.1089` n `12`; crypto_alt avg `-0.2787` n `228`; crypto_major avg `-0.8049` n `8`; equity avg `-0.3575` n `74`; fx avg `0.0014` n `6`; index avg `0.0219` n `23`; metal avg `-0.048` n `18`; unknown avg `0.0703` n `425`
- 24h: commodity avg `-1.3084` n `12`; crypto_alt avg `-4.5796` n `228`; crypto_major avg `-4.4956` n `8`; equity avg `-7.2256` n `74`; fx avg `-0.2658` n `6`; index avg `-4.1955` n `23`; metal avg `-4.5452` n `18`; unknown avg `0.239` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
