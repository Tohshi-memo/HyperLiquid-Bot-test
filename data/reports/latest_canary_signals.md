# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T16:07:23.728478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `-0.1205` n `230`; crypto_major avg `-0.1201` n `8`; equity avg `-0.0416` n `96`; fx avg `-0.0015` n `6`; index avg `-0.0255` n `25`; metal avg `-0.0217` n `20`; unknown avg `-0.0418` n `770`
- 1h: commodity avg `0.0153` n `12`; crypto_alt avg `-0.1115` n `230`; crypto_major avg `-0.1991` n `8`; equity avg `-0.0497` n `96`; fx avg `0.0025` n `6`; index avg `-0.0342` n `25`; metal avg `-0.0228` n `20`; unknown avg `-0.0521` n `770`
- 4h: commodity avg `0.0613` n `12`; crypto_alt avg `0.1599` n `230`; crypto_major avg `0.079` n `8`; equity avg `-0.0528` n `96`; fx avg `0.0059` n `6`; index avg `-0.0378` n `25`; metal avg `-0.0081` n `20`; unknown avg `-0.012` n `770`
- 24h: commodity avg `0.2492` n `12`; crypto_alt avg `0.3444` n `230`; crypto_major avg `0.9436` n `8`; equity avg `0.2672` n `96`; fx avg `0.0415` n `6`; index avg `-0.0594` n `25`; metal avg `-0.0442` n `20`; unknown avg `0.0867` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1384`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1307`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1156`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
