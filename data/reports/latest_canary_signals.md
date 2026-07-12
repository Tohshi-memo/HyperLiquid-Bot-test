# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T11:48:13.434505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.045` n `12`; crypto_alt avg `0.0804` n `230`; crypto_major avg `0.0912` n `8`; equity avg `-0.0132` n `92`; fx avg `0.0043` n `6`; index avg `0.0088` n `25`; metal avg `0.0075` n `20`; unknown avg `-0.0091` n `765`
- 1h: commodity avg `-0.0251` n `12`; crypto_alt avg `0.1439` n `230`; crypto_major avg `0.4145` n `8`; equity avg `0.0759` n `92`; fx avg `-0.0013` n `6`; index avg `0.0051` n `25`; metal avg `0.0077` n `20`; unknown avg `-0.0973` n `763`
- 4h: commodity avg `-0.0182` n `12`; crypto_alt avg `0.2148` n `230`; crypto_major avg `0.5436` n `8`; equity avg `0.1071` n `92`; fx avg `0.0013` n `6`; index avg `0.0133` n `25`; metal avg `0.0023` n `20`; unknown avg `-0.0112` n `763`
- 24h: commodity avg `0.4537` n `12`; crypto_alt avg `-0.8002` n `230`; crypto_major avg `-0.423` n `8`; equity avg `-0.1443` n `92`; fx avg `0.0067` n `6`; index avg `-0.1179` n `25`; metal avg `-0.0929` n `20`; unknown avg `0.1213` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
