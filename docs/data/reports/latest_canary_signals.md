# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T01:07:18.821362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1742` n `12`; crypto_alt avg `-0.0525` n `228`; crypto_major avg `-0.0768` n `8`; equity avg `0.0217` n `67`; fx avg `0.0033` n `6`; index avg `0.0047` n `23`; metal avg `-0.0879` n `18`; unknown avg `-0.3039` n `396`
- 1h: commodity avg `0.0164` n `12`; crypto_alt avg `0.0291` n `228`; crypto_major avg `-0.1285` n `8`; equity avg `0.1312` n `67`; fx avg `-0.0506` n `6`; index avg `0.1533` n `23`; metal avg `-0.0856` n `18`; unknown avg `-0.403` n `396`
- 4h: commodity avg `-0.7538` n `12`; crypto_alt avg `0.2716` n `228`; crypto_major avg `0.2587` n `8`; equity avg `0.0519` n `67`; fx avg `-0.1062` n `6`; index avg `0.17` n `23`; metal avg `1.3466` n `18`; unknown avg `-0.0829` n `396`
- 24h: commodity avg `0.2776` n `12`; crypto_alt avg `-1.5345` n `228`; crypto_major avg `0.0465` n `8`; equity avg `0.3173` n `67`; fx avg `-0.0286` n `6`; index avg `-0.1443` n `23`; metal avg `0.8726` n `18`; unknown avg `-0.5045` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
