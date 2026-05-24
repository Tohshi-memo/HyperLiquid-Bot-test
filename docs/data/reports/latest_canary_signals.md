# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T19:07:21.622012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0463` n `12`; crypto_alt avg `0.1227` n `228`; crypto_major avg `0.1103` n `8`; equity avg `0.0081` n `67`; fx avg `0.0042` n `6`; index avg `0.0131` n `23`; metal avg `0.0025` n `18`; unknown avg `0.0301` n `396`
- 1h: commodity avg `0.0282` n `12`; crypto_alt avg `-0.0723` n `228`; crypto_major avg `0.1266` n `8`; equity avg `-0.0248` n `67`; fx avg `0.0056` n `6`; index avg `-0.0105` n `23`; metal avg `-0.0258` n `18`; unknown avg `-0.2799` n `396`
- 4h: commodity avg `-0.0993` n `12`; crypto_alt avg `0.3848` n `228`; crypto_major avg `0.3003` n `8`; equity avg `0.0418` n `67`; fx avg `0.014` n `6`; index avg `0.0059` n `23`; metal avg `0.1112` n `18`; unknown avg `-0.5023` n `396`
- 24h: commodity avg `-0.3738` n `12`; crypto_alt avg `-0.2943` n `228`; crypto_major avg `1.6737` n `8`; equity avg `1.1696` n `67`; fx avg `0.0889` n `6`; index avg `0.3365` n `23`; metal avg `0.4677` n `18`; unknown avg `0.6374` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
