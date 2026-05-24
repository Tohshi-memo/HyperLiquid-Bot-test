# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T11:52:15.256978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0207` n `12`; crypto_alt avg `0.0181` n `228`; crypto_major avg `-0.0656` n `8`; equity avg `-0.0014` n `67`; fx avg `-0.0146` n `6`; index avg `0.0083` n `23`; metal avg `-0.006` n `18`; unknown avg `0.0605` n `396`
- 1h: commodity avg `0.0224` n `12`; crypto_alt avg `0.0392` n `228`; crypto_major avg `0.221` n `8`; equity avg `0.0921` n `67`; fx avg `-0.0138` n `6`; index avg `-0.0407` n `23`; metal avg `0.0227` n `18`; unknown avg `0.2452` n `396`
- 4h: commodity avg `0.2067` n `12`; crypto_alt avg `0.0916` n `228`; crypto_major avg `0.6442` n `8`; equity avg `0.2337` n `67`; fx avg `-0.0133` n `6`; index avg `-0.0746` n `23`; metal avg `0.0054` n `18`; unknown avg `-0.0158` n `396`
- 24h: commodity avg `-2.7025` n `12`; crypto_alt avg `3.9088` n `228`; crypto_major avg `4.7619` n `8`; equity avg `2.7992` n `67`; fx avg `0.0531` n `6`; index avg `1.2906` n `23`; metal avg `1.34` n `18`; unknown avg `1.4232` n `386`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
