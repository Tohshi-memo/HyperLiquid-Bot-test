# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T07:24:12.889893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0263` n `12`; crypto_alt avg `0.0897` n `228`; crypto_major avg `0.1777` n `8`; equity avg `0.0235` n `69`; fx avg `0.0006` n `6`; index avg `0.0571` n `23`; metal avg `-0.0001` n `18`; unknown avg `0.0447` n `421`
- 1h: commodity avg `0.0348` n `12`; crypto_alt avg `-0.168` n `228`; crypto_major avg `0.1257` n `8`; equity avg `0.0624` n `69`; fx avg `0.0005` n `6`; index avg `0.0621` n `23`; metal avg `0.0094` n `18`; unknown avg `-0.2823` n `421`
- 4h: commodity avg `-0.09` n `12`; crypto_alt avg `-0.4602` n `228`; crypto_major avg `0.1312` n `8`; equity avg `0.13` n `69`; fx avg `0.0043` n `6`; index avg `0.1539` n `23`; metal avg `-0.0053` n `18`; unknown avg `0.1391` n `401`
- 24h: commodity avg `-0.4272` n `12`; crypto_alt avg `0.9267` n `228`; crypto_major avg `1.7111` n `8`; equity avg `0.8621` n `69`; fx avg `0.0456` n `6`; index avg `0.1728` n `23`; metal avg `0.0314` n `18`; unknown avg `0.3769` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1914`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
