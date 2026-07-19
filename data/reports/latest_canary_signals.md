# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T15:22:29.085230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `12`; crypto_alt avg `-0.0089` n `230`; crypto_major avg `-0.0747` n `8`; equity avg `-0.0026` n `96`; fx avg `0.0008` n `6`; index avg `0.0003` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.0128` n `770`
- 1h: commodity avg `0.0186` n `12`; crypto_alt avg `0.1409` n `230`; crypto_major avg `0.1708` n `8`; equity avg `-0.0572` n `96`; fx avg `0.0001` n `6`; index avg `-0.0077` n `25`; metal avg `-0.0029` n `20`; unknown avg `0.024` n `770`
- 4h: commodity avg `0.0727` n `12`; crypto_alt avg `-0.1354` n `230`; crypto_major avg `-0.1771` n `8`; equity avg `-0.1106` n `96`; fx avg `-0.0088` n `6`; index avg `-0.0146` n `25`; metal avg `0.0103` n `20`; unknown avg `-0.033` n `770`
- 24h: commodity avg `0.2097` n `12`; crypto_alt avg `0.3319` n `230`; crypto_major avg `0.9893` n `8`; equity avg `0.2165` n `96`; fx avg `0.0002` n `6`; index avg `-0.0303` n `25`; metal avg `-0.0436` n `20`; unknown avg `0.0788` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1316`, n `666`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1268`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
