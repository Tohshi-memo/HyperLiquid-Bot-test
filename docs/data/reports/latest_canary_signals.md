# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T03:52:28.756840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0182` n `12`; crypto_alt avg `-0.0075` n `230`; crypto_major avg `-0.018` n `8`; equity avg `0.0098` n `96`; fx avg `-0.0021` n `6`; index avg `0.0049` n `25`; metal avg `-0.0038` n `20`; unknown avg `-0.131` n `769`
- 1h: commodity avg `-0.0585` n `12`; crypto_alt avg `-0.0794` n `230`; crypto_major avg `-0.0371` n `8`; equity avg `-0.0298` n `96`; fx avg `0.0006` n `6`; index avg `0.0198` n `25`; metal avg `0.0046` n `20`; unknown avg `-0.2106` n `769`
- 4h: commodity avg `-0.0486` n `12`; crypto_alt avg `-0.1384` n `230`; crypto_major avg `-0.0078` n `8`; equity avg `0.1919` n `96`; fx avg `-0.0104` n `6`; index avg `0.0693` n `25`; metal avg `0.0341` n `20`; unknown avg `-0.434` n `769`
- 24h: commodity avg `0.7287` n `12`; crypto_alt avg `-0.4677` n `230`; crypto_major avg `-0.2263` n `8`; equity avg `0.5799` n `96`; fx avg `0.0372` n `6`; index avg `0.0426` n `25`; metal avg `0.1324` n `20`; unknown avg `0.204` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
