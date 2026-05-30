# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T22:43:22.731784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0284` n `12`; crypto_alt avg `-0.209` n `228`; crypto_major avg `-0.1115` n `8`; equity avg `-0.0043` n `69`; fx avg `0.0006` n `6`; index avg `-0.0312` n `23`; metal avg `-0.0187` n `18`; unknown avg `-0.1453` n `421`
- 1h: commodity avg `0.0497` n `12`; crypto_alt avg `-0.9593` n `228`; crypto_major avg `-0.573` n `8`; equity avg `-0.1122` n `69`; fx avg `0.0019` n `6`; index avg `-0.0202` n `23`; metal avg `-0.0093` n `18`; unknown avg `0.8277` n `421`
- 4h: commodity avg `0.1787` n `12`; crypto_alt avg `-0.7483` n `228`; crypto_major avg `-0.4842` n `8`; equity avg `0.1518` n `69`; fx avg `0.009` n `6`; index avg `-0.0294` n `23`; metal avg `-0.0257` n `18`; unknown avg `0.7306` n `421`
- 24h: commodity avg `-0.044` n `12`; crypto_alt avg `1.0473` n `228`; crypto_major avg `2.3899` n `8`; equity avg `0.9144` n `69`; fx avg `0.0299` n `6`; index avg `0.0185` n `23`; metal avg `0.0352` n `18`; unknown avg `1.129` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
