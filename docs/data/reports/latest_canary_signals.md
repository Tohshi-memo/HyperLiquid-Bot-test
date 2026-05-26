# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T22:37:19.167276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `0.1331` n `228`; crypto_major avg `0.075` n `8`; equity avg `-0.0102` n `67`; fx avg `0.0053` n `6`; index avg `0.0409` n `23`; metal avg `-0.105` n `18`; unknown avg `0.0482` n `418`
- 1h: commodity avg `-0.2259` n `12`; crypto_alt avg `-0.168` n `228`; crypto_major avg `0.0279` n `8`; equity avg `-0.0155` n `67`; fx avg `0.0325` n `6`; index avg `-0.0515` n `23`; metal avg `-0.0375` n `18`; unknown avg `0.1089` n `418`
- 4h: commodity avg `-0.1196` n `12`; crypto_alt avg `-0.1163` n `228`; crypto_major avg `-0.4328` n `8`; equity avg `0.0035` n `67`; fx avg `0.0315` n `6`; index avg `-0.0126` n `23`; metal avg `0.4118` n `18`; unknown avg `-0.1846` n `418`
- 24h: commodity avg `0.8624` n `12`; crypto_alt avg `-1.1741` n `228`; crypto_major avg `-1.2711` n `8`; equity avg `-0.1801` n `67`; fx avg `-0.1172` n `6`; index avg `0.5275` n `23`; metal avg `-0.8458` n `18`; unknown avg `0.2687` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
