# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T10:37:30.428363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `12`; crypto_alt avg `0.2117` n `229`; crypto_major avg `0.1194` n `8`; equity avg `0.13` n `91`; fx avg `-0.0029` n `6`; index avg `0.0288` n `25`; metal avg `0.0232` n `20`; unknown avg `0.0952` n `766`
- 1h: commodity avg `0.0161` n `12`; crypto_alt avg `0.2413` n `229`; crypto_major avg `0.045` n `8`; equity avg `0.2501` n `91`; fx avg `-0.007` n `6`; index avg `0.0415` n `25`; metal avg `0.0692` n `20`; unknown avg `0.1676` n `766`
- 4h: commodity avg `-0.0938` n `12`; crypto_alt avg `0.7137` n `229`; crypto_major avg `0.7623` n `8`; equity avg `0.1914` n `91`; fx avg `0.0038` n `6`; index avg `0.0657` n `25`; metal avg `-0.0923` n `20`; unknown avg `1.2014` n `765`
- 24h: commodity avg `-1.0239` n `12`; crypto_alt avg `1.4604` n `229`; crypto_major avg `1.8718` n `8`; equity avg `0.6693` n `91`; fx avg `-0.1226` n `6`; index avg `0.2709` n `25`; metal avg `0.2458` n `20`; unknown avg `0.0503` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
