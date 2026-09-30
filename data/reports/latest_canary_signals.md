# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T17:37:34.388287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0124` n `12`; crypto_alt avg `-0.4709` n `234`; crypto_major avg `-0.4539` n `8`; equity avg `-0.0746` n `142`; fx avg `0.0073` n `6`; index avg `-0.0113` n `26`; metal avg `-0.0045` n `20`; unknown avg `0.1851` n `969`
- 1h: commodity avg `-0.0872` n `12`; crypto_alt avg `-0.6097` n `234`; crypto_major avg `-0.383` n `8`; equity avg `-0.2202` n `142`; fx avg `-0.007` n `6`; index avg `-0.0592` n `26`; metal avg `-0.0334` n `20`; unknown avg `3.2057` n `967`
- 4h: commodity avg `0.0049` n `12`; crypto_alt avg `-0.5631` n `234`; crypto_major avg `-0.464` n `8`; equity avg `-0.3739` n `142`; fx avg `0.0114` n `6`; index avg `-0.0602` n `26`; metal avg `-0.2146` n `20`; unknown avg `2.3543` n `875`
- 24h: commodity avg `0.0749` n `12`; crypto_alt avg `1.4218` n `234`; crypto_major avg `1.2252` n `8`; equity avg `-0.2015` n `142`; fx avg `0.0813` n `6`; index avg `0.0964` n `26`; metal avg `-0.013` n `20`; unknown avg `3.9739` n `820`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
