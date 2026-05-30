# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T21:22:16.270451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0355` n `12`; crypto_alt avg `0.0774` n `228`; crypto_major avg `0.0982` n `8`; equity avg `0.008` n `69`; fx avg `0.0006` n `6`; index avg `0.0769` n `23`; metal avg `-0.0063` n `18`; unknown avg `-0.0032` n `421`
- 1h: commodity avg `0.0481` n `12`; crypto_alt avg `0.0414` n `228`; crypto_major avg `0.059` n `8`; equity avg `0.0928` n `69`; fx avg `-0.0045` n `6`; index avg `0.082` n `23`; metal avg `0.0081` n `18`; unknown avg `0.2907` n `421`
- 4h: commodity avg `0.0041` n `12`; crypto_alt avg `0.3453` n `228`; crypto_major avg `0.3544` n `8`; equity avg `0.2472` n `69`; fx avg `0.0056` n `6`; index avg `0.0453` n `23`; metal avg `-0.0139` n `18`; unknown avg `-0.0245` n `421`
- 24h: commodity avg `-0.1466` n `12`; crypto_alt avg `1.6492` n `228`; crypto_major avg `2.7058` n `8`; equity avg `1.0164` n `69`; fx avg `0.0225` n `6`; index avg `0.1483` n `23`; metal avg `0.1127` n `18`; unknown avg `0.2926` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
