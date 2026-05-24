# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T16:52:15.746346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `12`; crypto_alt avg `0.1614` n `228`; crypto_major avg `0.1217` n `8`; equity avg `0.0676` n `67`; fx avg `-0.003` n `6`; index avg `0.0082` n `23`; metal avg `-0.0065` n `18`; unknown avg `-0.0276` n `396`
- 1h: commodity avg `0.0669` n `12`; crypto_alt avg `0.0228` n `228`; crypto_major avg `0.0869` n `8`; equity avg `0.1355` n `67`; fx avg `0.0207` n `6`; index avg `0.0025` n `23`; metal avg `0.0213` n `18`; unknown avg `0.0818` n `396`
- 4h: commodity avg `0.7164` n `12`; crypto_alt avg `-0.5025` n `228`; crypto_major avg `-0.6494` n `8`; equity avg `-0.3464` n `67`; fx avg `0.0425` n `6`; index avg `-0.3515` n `23`; metal avg `-0.3452` n `18`; unknown avg `0.0539` n `396`
- 24h: commodity avg `-1.2347` n `12`; crypto_alt avg `0.4083` n `228`; crypto_major avg `2.1827` n `8`; equity avg `1.6022` n `67`; fx avg `0.0913` n `6`; index avg `0.5963` n `23`; metal avg `0.6285` n `18`; unknown avg `0.6982` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
