# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T01:52:26.575434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `12`; crypto_alt avg `-0.1215` n `230`; crypto_major avg `-0.2177` n `8`; equity avg `-0.274` n `98`; fx avg `0.0098` n `6`; index avg `-0.0592` n `25`; metal avg `-0.0154` n `20`; unknown avg `-0.0859` n `771`
- 1h: commodity avg `-0.0538` n `12`; crypto_alt avg `-0.2396` n `230`; crypto_major avg `-0.2455` n `8`; equity avg `-0.0918` n `98`; fx avg `0.017` n `6`; index avg `0.0701` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.1508` n `771`
- 4h: commodity avg `-0.0079` n `12`; crypto_alt avg `0.0721` n `230`; crypto_major avg `0.0261` n `8`; equity avg `0.1794` n `98`; fx avg `0.0459` n `6`; index avg `0.111` n `25`; metal avg `0.0941` n `20`; unknown avg `-0.5439` n `770`
- 24h: commodity avg `-0.3415` n `12`; crypto_alt avg `1.0921` n `230`; crypto_major avg `0.8309` n `8`; equity avg `0.0127` n `98`; fx avg `-0.0943` n `6`; index avg `0.067` n `25`; metal avg `0.2335` n `20`; unknown avg `-0.156` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0854`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0729`, n `666`, weak_sample_signal
