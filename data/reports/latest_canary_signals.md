# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T05:37:26.047148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.1231` n `230`; crypto_major avg `-0.1584` n `8`; equity avg `-0.0023` n `96`; fx avg `0.0036` n `6`; index avg `-0.0041` n `25`; metal avg `-0.0026` n `20`; unknown avg `0.0601` n `770`
- 1h: commodity avg `0.0122` n `12`; crypto_alt avg `-0.0732` n `230`; crypto_major avg `-0.1359` n `8`; equity avg `-0.0077` n `96`; fx avg `0.0194` n `6`; index avg `-0.0024` n `25`; metal avg `-0.0067` n `20`; unknown avg `1.9003` n `770`
- 4h: commodity avg `-0.0846` n `12`; crypto_alt avg `0.0004` n `230`; crypto_major avg `0.1067` n `8`; equity avg `0.1368` n `96`; fx avg `0.0164` n `6`; index avg `0.0006` n `25`; metal avg `0.0217` n `20`; unknown avg `0.571` n `770`
- 24h: commodity avg `0.3332` n `12`; crypto_alt avg `0.0795` n `230`; crypto_major avg `0.8194` n `8`; equity avg `-0.052` n `96`; fx avg `-0.0158` n `6`; index avg `-0.07` n `25`; metal avg `-0.0283` n `20`; unknown avg `0.0888` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
