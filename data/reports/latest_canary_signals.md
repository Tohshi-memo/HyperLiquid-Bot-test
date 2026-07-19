# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T10:58:42.739631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: crypto_alt avg `0.1612` n `225`; crypto_major avg `0.0724` n `7`; metal avg `0.03` n `1`; unknown avg `-0.0055` n `703`
- 1h: commodity avg `-0.018` n `12`; crypto_alt avg `0.2003` n `230`; crypto_major avg `0.1112` n `8`; equity avg `-0.0285` n `96`; fx avg `0.0176` n `6`; index avg `-0.0001` n `25`; metal avg `0.0037` n `20`; unknown avg `0.0794` n `770`
- 4h: commodity avg `-0.0139` n `12`; crypto_alt avg `0.0588` n `230`; crypto_major avg `0.0854` n `8`; equity avg `0.0708` n `96`; fx avg `0.0101` n `6`; index avg `0.0277` n `25`; metal avg `-0.0543` n `20`; unknown avg `-0.0609` n `770`
- 24h: commodity avg `0.2063` n `12`; crypto_alt avg `0.5793` n `230`; crypto_major avg `1.1154` n `8`; equity avg `0.1993` n `96`; fx avg `-0.0038` n `6`; index avg `-0.0311` n `25`; metal avg `-0.0748` n `20`; unknown avg `0.1392` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1114`, n `667`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.111`, n `667`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0988`, n `667`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `667`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
