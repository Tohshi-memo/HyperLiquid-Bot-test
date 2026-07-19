# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T14:07:23.969461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `12`; crypto_alt avg `0.0626` n `230`; crypto_major avg `0.0376` n `8`; equity avg `-0.0181` n `96`; fx avg `0.0007` n `6`; index avg `0.0068` n `25`; metal avg `-0.0102` n `20`; unknown avg `-0.0005` n `770`
- 1h: commodity avg `-0.0094` n `12`; crypto_alt avg `0.1502` n `230`; crypto_major avg `0.2521` n `8`; equity avg `0.0451` n `96`; fx avg `0.0061` n `6`; index avg `0.0043` n `25`; metal avg `0.0143` n `20`; unknown avg `0.084` n `770`
- 4h: commodity avg `-0.0069` n `12`; crypto_alt avg `-0.0121` n `230`; crypto_major avg `0.1387` n `8`; equity avg `0.0267` n `96`; fx avg `0.0153` n `6`; index avg `-0.0068` n `25`; metal avg `0.0007` n `20`; unknown avg `0.0319` n `770`
- 24h: commodity avg `0.2248` n `12`; crypto_alt avg `0.673` n `230`; crypto_major avg `1.2354` n `8`; equity avg `0.3069` n `96`; fx avg `-0.0032` n `6`; index avg `-0.0283` n `25`; metal avg `-0.066` n `20`; unknown avg `0.1784` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1255`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1226`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0997`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0907`, n `666`, weak_sample_signal
