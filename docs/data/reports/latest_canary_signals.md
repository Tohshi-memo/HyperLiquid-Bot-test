# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T08:52:27.494769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `0.1125` n `230`; crypto_major avg `0.2019` n `8`; equity avg `0.0708` n `96`; fx avg `0.0005` n `6`; index avg `0.009` n `25`; metal avg `-0.0087` n `20`; unknown avg `0.0853` n `770`
- 1h: commodity avg `0.0034` n `12`; crypto_alt avg `0.1297` n `230`; crypto_major avg `0.2094` n `8`; equity avg `0.1366` n `96`; fx avg `-0.012` n `6`; index avg `0.024` n `25`; metal avg `-0.0119` n `20`; unknown avg `0.0062` n `770`
- 4h: commodity avg `0.0592` n `12`; crypto_alt avg `0.1853` n `230`; crypto_major avg `0.2575` n `8`; equity avg `0.2537` n `96`; fx avg `0.0222` n `6`; index avg `0.0392` n `25`; metal avg `-0.0349` n `20`; unknown avg `0.0463` n `752`
- 24h: commodity avg `0.3269` n `12`; crypto_alt avg `0.4236` n `230`; crypto_major avg `1.1904` n `8`; equity avg `0.3034` n `96`; fx avg `-0.0158` n `6`; index avg `-0.0369` n `25`; metal avg `-0.0663` n `20`; unknown avg `0.0413` n `751`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
