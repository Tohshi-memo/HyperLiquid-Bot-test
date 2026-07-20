# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T10:22:31.498346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `12`; crypto_alt avg `0.1046` n `230`; crypto_major avg `0.1572` n `8`; equity avg `0.0985` n `98`; fx avg `0.0124` n `6`; index avg `0.0064` n `25`; metal avg `0.0134` n `20`; unknown avg `0.0719` n `770`
- 1h: commodity avg `0.0299` n `12`; crypto_alt avg `0.2218` n `230`; crypto_major avg `0.1993` n `8`; equity avg `0.2451` n `98`; fx avg `0.0173` n `6`; index avg `0.0427` n `25`; metal avg `0.0389` n `20`; unknown avg `0.0136` n `770`
- 4h: commodity avg `-0.5869` n `12`; crypto_alt avg `0.8728` n `230`; crypto_major avg `0.4077` n `8`; equity avg `0.6671` n `98`; fx avg `0.0354` n `6`; index avg `0.1302` n `25`; metal avg `0.2075` n `20`; unknown avg `0.048` n `763`
- 24h: commodity avg `-0.5849` n `12`; crypto_alt avg `0.3365` n `230`; crypto_major avg `-0.1442` n `8`; equity avg `0.4934` n `97`; fx avg `-0.0038` n `6`; index avg `0.1107` n `25`; metal avg `0.2364` n `20`; unknown avg `0.0082` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0974`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0922`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0847`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0749`, n `666`, weak_sample_signal
