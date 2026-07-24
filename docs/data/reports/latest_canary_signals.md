# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T23:51:01.910695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0221` n `12`; crypto_alt avg `0.0425` n `230`; crypto_major avg `0.072` n `8`; equity avg `0.0209` n `100`; fx avg `-0.0041` n `6`; index avg `0.0058` n `25`; metal avg `-0.0007` n `20`; unknown avg `0.011` n `774`
- 1h: commodity avg `-0.0175` n `12`; crypto_alt avg `-0.0032` n `230`; crypto_major avg `0.1072` n `8`; equity avg `-0.2143` n `100`; fx avg `0.0398` n `6`; index avg `-0.0211` n `25`; metal avg `-0.004` n `20`; unknown avg `-0.0717` n `774`
- 4h: commodity avg `0.2007` n `12`; crypto_alt avg `-0.061` n `230`; crypto_major avg `-0.0253` n `8`; equity avg `0.0308` n `100`; fx avg `0.023` n `6`; index avg `0.0006` n `25`; metal avg `0.0214` n `20`; unknown avg `-0.1076` n `773`
- 24h: commodity avg `-0.3383` n `12`; crypto_alt avg `-0.845` n `230`; crypto_major avg `-0.7921` n `8`; equity avg `-3.3204` n `100`; fx avg `-0.1286` n `6`; index avg `-0.4801` n `25`; metal avg `0.0231` n `20`; unknown avg `13.983` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1285`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1229`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1135`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1114`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1086`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
