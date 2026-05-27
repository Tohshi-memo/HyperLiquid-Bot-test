# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T01:52:21.709026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1281` n `12`; crypto_alt avg `0.0887` n `228`; crypto_major avg `0.0915` n `8`; equity avg `-0.102` n `67`; fx avg `-0.0028` n `6`; index avg `-0.0504` n `23`; metal avg `-0.2558` n `18`; unknown avg `0.0411` n `418`
- 1h: commodity avg `-0.1556` n `12`; crypto_alt avg `-0.2596` n `228`; crypto_major avg `-0.1305` n `8`; equity avg `-0.0133` n `67`; fx avg `-0.0231` n `6`; index avg `-0.0257` n `23`; metal avg `-0.4461` n `18`; unknown avg `-0.067` n `418`
- 4h: commodity avg `-0.1055` n `12`; crypto_alt avg `0.1653` n `228`; crypto_major avg `0.3025` n `8`; equity avg `0.1255` n `67`; fx avg `-0.0125` n `6`; index avg `0.1401` n `23`; metal avg `-0.1091` n `18`; unknown avg `0.561` n `418`
- 24h: commodity avg `-0.0771` n `12`; crypto_alt avg `0.0654` n `228`; crypto_major avg `-0.1048` n `8`; equity avg `0.9761` n `67`; fx avg `-0.0487` n `6`; index avg `1.0504` n `23`; metal avg `0.1302` n `18`; unknown avg `0.7047` n `397`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1611`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
