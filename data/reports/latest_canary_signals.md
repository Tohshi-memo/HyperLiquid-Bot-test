# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T16:21:21.763691+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0378` n `12`; crypto_alt avg `-0.1314` n `228`; crypto_major avg `-0.1076` n `8`; equity avg `-0.0785` n `69`; fx avg `-0.0014` n `6`; index avg `0.0334` n `23`; metal avg `-0.0053` n `18`; unknown avg `-0.0582` n `421`
- 1h: commodity avg `0.0776` n `12`; crypto_alt avg `-0.2839` n `228`; crypto_major avg `-0.272` n `8`; equity avg `0.0533` n `69`; fx avg `-0.0153` n `6`; index avg `0.1145` n `23`; metal avg `-0.0427` n `18`; unknown avg `-0.2576` n `421`
- 4h: commodity avg `0.1977` n `12`; crypto_alt avg `-1.1313` n `228`; crypto_major avg `-0.4557` n `8`; equity avg `0.0316` n `69`; fx avg `-0.021` n `6`; index avg `0.1749` n `23`; metal avg `-0.0864` n `18`; unknown avg `-0.669` n `421`
- 24h: commodity avg `0.8791` n `12`; crypto_alt avg `-0.9985` n `228`; crypto_major avg `0.0663` n `8`; equity avg `0.8982` n `69`; fx avg `-0.0269` n `6`; index avg `0.0585` n `23`; metal avg `-0.1494` n `18`; unknown avg `-0.0125` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
