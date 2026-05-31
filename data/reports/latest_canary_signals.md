# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T00:07:20.779273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0269` n `12`; crypto_alt avg `0.0679` n `228`; crypto_major avg `0.0849` n `8`; equity avg `0.0301` n `69`; fx avg `0.0223` n `6`; index avg `-0.0199` n `23`; metal avg `0.0037` n `18`; unknown avg `0.8002` n `421`
- 1h: commodity avg `-0.0669` n `12`; crypto_alt avg `-0.071` n `228`; crypto_major avg `0.1042` n `8`; equity avg `0.0608` n `69`; fx avg `0.0067` n `6`; index avg `0.0144` n `23`; metal avg `0.0021` n `18`; unknown avg `-0.0625` n `421`
- 4h: commodity avg `0.1127` n `12`; crypto_alt avg `-0.7822` n `228`; crypto_major avg `-0.2745` n `8`; equity avg `0.2382` n `69`; fx avg `-0.0101` n `6`; index avg `0.1758` n `23`; metal avg `-0.0152` n `18`; unknown avg `0.6564` n `421`
- 24h: commodity avg `-0.3281` n `12`; crypto_alt avg `0.8999` n `228`; crypto_major avg `2.6702` n `8`; equity avg `1.2064` n `69`; fx avg `0.0297` n `6`; index avg `0.0404` n `23`; metal avg `0.0068` n `18`; unknown avg `0.2188` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1728`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
