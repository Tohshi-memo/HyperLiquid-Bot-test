# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T18:37:21.154197+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0408` n `12`; crypto_alt avg `0.1558` n `228`; crypto_major avg `0.0854` n `8`; equity avg `-0.0324` n `69`; fx avg `0.0` n `6`; index avg `-0.0107` n `23`; metal avg `0.0116` n `18`; unknown avg `0.0793` n `421`
- 1h: commodity avg `0.1021` n `12`; crypto_alt avg `0.0404` n `228`; crypto_major avg `-0.0626` n `8`; equity avg `-0.0213` n `69`; fx avg `0.0021` n `6`; index avg `-0.0161` n `23`; metal avg `0.0121` n `18`; unknown avg `-0.3406` n `421`
- 4h: commodity avg `0.1718` n `12`; crypto_alt avg `-0.0751` n `228`; crypto_major avg `-0.3158` n `8`; equity avg `0.0997` n `69`; fx avg `-0.0039` n `6`; index avg `0.2283` n `23`; metal avg `-0.0639` n `18`; unknown avg `0.0538` n `421`
- 24h: commodity avg `0.7691` n `12`; crypto_alt avg `-1.2762` n `228`; crypto_major avg `-0.6917` n `8`; equity avg `0.895` n `69`; fx avg `-0.0086` n `6`; index avg `0.1252` n `23`; metal avg `-0.1419` n `18`; unknown avg `0.3397` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2243`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
