# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T21:22:33.765356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `0.0861` n `230`; crypto_major avg `0.0193` n `8`; equity avg `0.2339` n `102`; fx avg `-0.0134` n `6`; index avg `0.0354` n `25`; metal avg `0.0006` n `20`; unknown avg `-0.0591` n `779`
- 1h: commodity avg `-0.0046` n `12`; crypto_alt avg `-0.1124` n `230`; crypto_major avg `-0.1154` n `8`; equity avg `0.2747` n `102`; fx avg `-0.0083` n `6`; index avg `-0.0274` n `25`; metal avg `-0.0329` n `20`; unknown avg `-0.039` n `779`
- 4h: commodity avg `-0.015` n `12`; crypto_alt avg `0.1239` n `230`; crypto_major avg `-0.015` n `8`; equity avg `1.097` n `102`; fx avg `-0.0683` n `6`; index avg `0.1267` n `25`; metal avg `0.1008` n `20`; unknown avg `-0.1435` n `779`
- 24h: commodity avg `-0.1385` n `12`; crypto_alt avg `1.7408` n `230`; crypto_major avg `2.2359` n `8`; equity avg `8.3666` n `102`; fx avg `-0.4069` n `6`; index avg `1.0303` n `25`; metal avg `0.7` n `20`; unknown avg `0.2442` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
