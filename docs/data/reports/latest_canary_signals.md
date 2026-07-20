# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T09:37:29.009943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0538` n `12`; crypto_alt avg `0.0872` n `230`; crypto_major avg `0.098` n `8`; equity avg `0.0763` n `98`; fx avg `0.0017` n `6`; index avg `0.0192` n `25`; metal avg `0.0011` n `20`; unknown avg `0.0442` n `770`
- 1h: commodity avg `-0.0769` n `12`; crypto_alt avg `0.5534` n `230`; crypto_major avg `0.4384` n `8`; equity avg `0.2984` n `98`; fx avg `-0.0225` n `6`; index avg `0.069` n `25`; metal avg `-0.0541` n `20`; unknown avg `0.0626` n `770`
- 4h: commodity avg `-0.5683` n `12`; crypto_alt avg `0.8457` n `230`; crypto_major avg `0.3422` n `8`; equity avg `0.3379` n `98`; fx avg `-0.0061` n `6`; index avg `0.1064` n `25`; metal avg `0.1938` n `20`; unknown avg `0.0463` n `747`
- 24h: commodity avg `-0.6739` n `12`; crypto_alt avg `0.1786` n `230`; crypto_major avg `-0.2945` n `8`; equity avg `0.3084` n `97`; fx avg `-0.0343` n `6`; index avg `0.0787` n `25`; metal avg `0.1984` n `20`; unknown avg `0.0265` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0893`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0803`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0765`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
