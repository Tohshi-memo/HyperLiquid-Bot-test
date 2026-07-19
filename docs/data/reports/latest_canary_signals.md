# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T09:07:24.288502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `12`; crypto_alt avg `0.0407` n `230`; crypto_major avg `0.0057` n `8`; equity avg `-0.021` n `96`; fx avg `-0.0096` n `6`; index avg `0.0077` n `25`; metal avg `-0.0163` n `20`; unknown avg `-0.0633` n `770`
- 1h: commodity avg `0.0434` n `12`; crypto_alt avg `0.0823` n `230`; crypto_major avg `0.1405` n `8`; equity avg `0.0568` n `96`; fx avg `-0.0273` n `6`; index avg `0.0259` n `25`; metal avg `-0.027` n `20`; unknown avg `-0.0574` n `770`
- 4h: commodity avg `0.0648` n `12`; crypto_alt avg `0.1236` n `230`; crypto_major avg `0.2157` n `8`; equity avg `0.1896` n `96`; fx avg `0.0034` n `6`; index avg `0.0467` n `25`; metal avg `-0.044` n `20`; unknown avg `0.0428` n `752`
- 24h: commodity avg `0.3251` n `12`; crypto_alt avg `0.6153` n `230`; crypto_major avg `1.2794` n `8`; equity avg `0.2741` n `96`; fx avg `-0.0238` n `6`; index avg `-0.0398` n `25`; metal avg `-0.0815` n `20`; unknown avg `0.0588` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
