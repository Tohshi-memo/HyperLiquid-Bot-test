# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T13:07:20.565519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `12`; crypto_alt avg `0.0076` n `228`; crypto_major avg `-0.0089` n `8`; equity avg `-0.0618` n `69`; fx avg `-0.0036` n `6`; index avg `-0.009` n `23`; metal avg `0.0004` n `18`; unknown avg `-0.0412` n `421`
- 1h: commodity avg `-0.0047` n `12`; crypto_alt avg `0.2055` n `228`; crypto_major avg `0.138` n `8`; equity avg `0.0245` n `69`; fx avg `-0.0036` n `6`; index avg `-0.0311` n `23`; metal avg `0.0075` n `18`; unknown avg `-0.1001` n `421`
- 4h: commodity avg `0.1198` n `12`; crypto_alt avg `0.2065` n `228`; crypto_major avg `-0.0163` n `8`; equity avg `-0.0877` n `69`; fx avg `-0.02` n `6`; index avg `-0.1065` n `23`; metal avg `-0.0119` n `18`; unknown avg `-0.5472` n `421`
- 24h: commodity avg `0.1298` n `12`; crypto_alt avg `0.048` n `228`; crypto_major avg `1.0352` n `8`; equity avg `0.8496` n `69`; fx avg `-0.0144` n `6`; index avg `-0.239` n `23`; metal avg `-0.0409` n `18`; unknown avg `0.3507` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
