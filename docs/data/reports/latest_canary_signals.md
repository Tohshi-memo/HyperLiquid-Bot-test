# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T14:37:17.483281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `0.1772` n `228`; crypto_major avg `0.3356` n `8`; equity avg `0.0231` n `69`; fx avg `0.0011` n `6`; index avg `0.0132` n `23`; metal avg `0.0029` n `18`; unknown avg `0.1674` n `421`
- 1h: commodity avg `0.046` n `12`; crypto_alt avg `0.5868` n `228`; crypto_major avg `0.6622` n `8`; equity avg `0.1159` n `69`; fx avg `0.0194` n `6`; index avg `0.1237` n `23`; metal avg `0.0182` n `18`; unknown avg `0.1642` n `421`
- 4h: commodity avg `0.2617` n `12`; crypto_alt avg `0.3097` n `228`; crypto_major avg `0.7744` n `8`; equity avg `0.3523` n `69`; fx avg `0.0198` n `6`; index avg `0.1827` n `23`; metal avg `-0.04` n `18`; unknown avg `0.1416` n `421`
- 24h: commodity avg `-0.3824` n `12`; crypto_alt avg `3.3477` n `228`; crypto_major avg `3.7636` n `8`; equity avg `2.1643` n `69`; fx avg `0.1135` n `6`; index avg `0.5121` n `23`; metal avg `0.3127` n `18`; unknown avg `0.5262` n `400`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1919`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1812`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
