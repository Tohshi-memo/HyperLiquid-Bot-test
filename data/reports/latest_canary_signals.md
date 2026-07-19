# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T08:07:31.477437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `12`; crypto_alt avg `0.0877` n `230`; crypto_major avg `0.0743` n `8`; equity avg `0.0587` n `96`; fx avg `0.0057` n `6`; index avg `0.0058` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.0011` n `770`
- 1h: commodity avg `0.0088` n `12`; crypto_alt avg `0.0471` n `230`; crypto_major avg `0.0934` n `8`; equity avg `0.1046` n `96`; fx avg `0.0211` n `6`; index avg `0.0155` n `25`; metal avg `-0.0291` n `20`; unknown avg `0.0297` n `770`
- 4h: commodity avg `0.0221` n `12`; crypto_alt avg `0.2096` n `230`; crypto_major avg `0.2628` n `8`; equity avg `0.1477` n `96`; fx avg `0.0232` n `6`; index avg `0.0077` n `25`; metal avg `-0.0104` n `20`; unknown avg `0.0491` n `752`
- 24h: commodity avg `0.3214` n `12`; crypto_alt avg `0.3955` n `230`; crypto_major avg `1.0882` n `8`; equity avg `0.1954` n `96`; fx avg `-0.0002` n `6`; index avg `-0.0136` n `25`; metal avg `-0.0581` n `20`; unknown avg `0.0569` n `751`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
