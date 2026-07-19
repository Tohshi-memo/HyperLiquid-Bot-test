# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T04:22:25.524153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `0.0206` n `230`; crypto_major avg `0.0311` n `8`; equity avg `-0.0184` n `96`; fx avg `-0.0006` n `6`; index avg `-0.0096` n `25`; metal avg `0.0013` n `20`; unknown avg `-0.0839` n `770`
- 1h: commodity avg `-0.0184` n `12`; crypto_alt avg `0.0108` n `230`; crypto_major avg `-0.0046` n `8`; equity avg `0.1059` n `96`; fx avg `0.0071` n `6`; index avg `-0.0311` n `25`; metal avg `-0.0132` n `20`; unknown avg `-0.2924` n `770`
- 4h: commodity avg `-0.0364` n `12`; crypto_alt avg `-0.1806` n `230`; crypto_major avg `0.0634` n `8`; equity avg `0.2661` n `96`; fx avg `0.0507` n `6`; index avg `-0.0006` n `25`; metal avg `0.0298` n `20`; unknown avg `-0.3929` n `770`
- 24h: commodity avg `0.343` n `12`; crypto_alt avg `-0.0977` n `230`; crypto_major avg `0.7487` n `8`; equity avg `-0.111` n `96`; fx avg `-0.021` n `6`; index avg `-0.0459` n `25`; metal avg `-0.0293` n `20`; unknown avg `0.0475` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
