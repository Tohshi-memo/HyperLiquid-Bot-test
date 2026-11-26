# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T03:37:38.236666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0255` n `13`; crypto_alt avg `-0.1101` n `239`; crypto_major avg `-0.1613` n `8`; equity avg `0.0192` n `168`; fx avg `-0.0035` n `6`; index avg `0.0111` n `27`; metal avg `0.0107` n `20`; unknown avg `1.492` n `1265`
- 1h: commodity avg `0.0654` n `13`; crypto_alt avg `-0.1876` n `239`; crypto_major avg `-0.1093` n `8`; equity avg `-0.211` n `168`; fx avg `0.0227` n `6`; index avg `-0.0223` n `27`; metal avg `-0.2085` n `20`; unknown avg `1.5664` n `1263`
- 4h: commodity avg `0.1015` n `13`; crypto_alt avg `1.1132` n `239`; crypto_major avg `0.8612` n `8`; equity avg `1.0352` n `168`; fx avg `-0.0349` n `6`; index avg `0.1018` n `27`; metal avg `0.1419` n `20`; unknown avg `1.8109` n `1247`
- 24h: commodity avg `0.7502` n `13`; crypto_alt avg `3.572` n `239`; crypto_major avg `2.5258` n `8`; equity avg `1.8889` n `168`; fx avg `-0.0004` n `6`; index avg `0.1482` n `27`; metal avg `0.5105` n `20`; unknown avg `771.7081` n `1015`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2002`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
