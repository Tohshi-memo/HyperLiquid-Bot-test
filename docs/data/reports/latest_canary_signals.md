# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T23:30:37.433986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0309` n `12`; crypto_alt avg `0.1026` n `228`; crypto_major avg `0.1001` n `8`; equity avg `-0.083` n `67`; fx avg `-0.0631` n `6`; index avg `-0.0146` n `23`; metal avg `0.0541` n `18`; unknown avg `0.0225` n `396`
- 1h: commodity avg `-0.1863` n `12`; crypto_alt avg `0.1795` n `228`; crypto_major avg `0.3706` n `8`; equity avg `-0.0761` n `67`; fx avg `-0.054` n `6`; index avg `-0.0876` n `23`; metal avg `0.5671` n `18`; unknown avg `0.8739` n `396`
- 4h: commodity avg `-0.7575` n `12`; crypto_alt avg `-0.3724` n `228`; crypto_major avg `-0.0204` n `8`; equity avg `-0.1435` n `67`; fx avg `0.0138` n `6`; index avg `-0.1254` n `23`; metal avg `1.4514` n `18`; unknown avg `0.7179` n `396`
- 24h: commodity avg `0.5` n `12`; crypto_alt avg `-1.7385` n `228`; crypto_major avg `0.5953` n `8`; equity avg `0.1424` n `67`; fx avg `0.0306` n `6`; index avg `-0.1569` n `23`; metal avg `1.2457` n `18`; unknown avg `1.2599` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
