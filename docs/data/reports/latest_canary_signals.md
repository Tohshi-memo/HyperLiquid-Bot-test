# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T01:36:04.264639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `0.0112` n `228`; crypto_major avg `-0.0782` n `8`; equity avg `-0.055` n `67`; fx avg `-0.0197` n `6`; index avg `0.0387` n `23`; metal avg `0.0516` n `18`; unknown avg `0.0826` n `396`
- 1h: commodity avg `0.0894` n `12`; crypto_alt avg `0.021` n `228`; crypto_major avg `-0.1085` n `8`; equity avg `-0.0351` n `67`; fx avg `-0.0502` n `6`; index avg `0.1044` n `23`; metal avg `-0.1066` n `18`; unknown avg `-0.2538` n `396`
- 4h: commodity avg `-0.6682` n `12`; crypto_alt avg `1.5305` n `228`; crypto_major avg `1.0527` n `8`; equity avg `0.1906` n `67`; fx avg `-0.1312` n `6`; index avg `0.2041` n `23`; metal avg `1.5277` n `18`; unknown avg `1.0521` n `396`
- 24h: commodity avg `0.4082` n `12`; crypto_alt avg `-1.4323` n `228`; crypto_major avg `-0.1805` n `8`; equity avg `0.1442` n `67`; fx avg `-0.0576` n `6`; index avg `-0.1827` n `23`; metal avg `0.7362` n `18`; unknown avg `-0.4295` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
