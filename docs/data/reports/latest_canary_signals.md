# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T21:06:03.425357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `-0.0361` n `230`; crypto_major avg `-0.0774` n `8`; equity avg `-0.0118` n `100`; fx avg `-0.0021` n `6`; index avg `-0.0161` n `25`; metal avg `-0.002` n `20`; unknown avg `0.0163` n `774`
- 1h: commodity avg `0.0005` n `12`; crypto_alt avg `-0.125` n `230`; crypto_major avg `-0.1879` n `8`; equity avg `0.0206` n `100`; fx avg `0.0029` n `6`; index avg `0.0062` n `25`; metal avg `-0.0018` n `20`; unknown avg `0.0564` n `774`
- 4h: commodity avg `-0.0479` n `12`; crypto_alt avg `0.0244` n `230`; crypto_major avg `0.0383` n `8`; equity avg `0.2065` n `100`; fx avg `-0.008` n `6`; index avg `0.0504` n `25`; metal avg `0.0225` n `20`; unknown avg `-0.1374` n `774`
- 24h: commodity avg `-0.6466` n `12`; crypto_alt avg `0.4755` n `230`; crypto_major avg `1.0442` n `8`; equity avg `0.3078` n `100`; fx avg `0.01` n `6`; index avg `0.132` n `25`; metal avg `0.0285` n `20`; unknown avg `-0.3357` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1345`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1214`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1209`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1162`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.114`, n `666`, weak_sample_signal
