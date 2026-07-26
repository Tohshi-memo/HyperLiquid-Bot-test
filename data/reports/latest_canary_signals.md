# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T05:22:32.342443+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `0.1756` n `230`; crypto_major avg `0.0845` n `8`; equity avg `-0.0096` n `100`; fx avg `-0.0027` n `6`; index avg `-0.0055` n `25`; metal avg `-0.0041` n `20`; unknown avg `-0.1074` n `775`
- 1h: commodity avg `-0.0146` n `12`; crypto_alt avg `0.2085` n `230`; crypto_major avg `0.2302` n `8`; equity avg `-0.0255` n `100`; fx avg `-0.0021` n `6`; index avg `-0.0065` n `25`; metal avg `0.001` n `20`; unknown avg `-0.1377` n `775`
- 4h: commodity avg `-0.0643` n `12`; crypto_alt avg `0.5625` n `230`; crypto_major avg `0.5526` n `8`; equity avg `0.1381` n `100`; fx avg `0.0712` n `6`; index avg `0.0293` n `25`; metal avg `0.022` n `20`; unknown avg `-0.0776` n `774`
- 24h: commodity avg `-0.5252` n `12`; crypto_alt avg `1.0688` n `230`; crypto_major avg `1.5737` n `8`; equity avg `0.4778` n `100`; fx avg `0.0681` n `6`; index avg `0.126` n `25`; metal avg `0.0529` n `20`; unknown avg `-0.1373` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1832`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1382`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1237`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.121`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1192`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1179`, n `666`, weak_sample_signal
