# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T20:37:31.130320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0577` n `12`; crypto_alt avg `0.0351` n `234`; crypto_major avg `0.0328` n `8`; equity avg `0.0254` n `142`; fx avg `0.0006` n `6`; index avg `0.0149` n `26`; metal avg `0.0299` n `20`; unknown avg `0.4021` n `938`
- 1h: commodity avg `-0.0853` n `12`; crypto_alt avg `-0.0111` n `234`; crypto_major avg `-0.0239` n `8`; equity avg `0.0794` n `142`; fx avg `0.0014` n `6`; index avg `0.0231` n `26`; metal avg `0.0376` n `20`; unknown avg `-1.0288` n `900`
- 4h: commodity avg `-0.3162` n `12`; crypto_alt avg `-0.0112` n `234`; crypto_major avg `-0.0914` n `8`; equity avg `0.0139` n `142`; fx avg `0.0025` n `6`; index avg `0.087` n `26`; metal avg `0.2457` n `20`; unknown avg `12.8716` n `900`
- 24h: commodity avg `-1.0119` n `12`; crypto_alt avg `0.9665` n `234`; crypto_major avg `-0.2792` n `8`; equity avg `0.741` n `142`; fx avg `-0.1667` n `6`; index avg `0.0989` n `26`; metal avg `0.2652` n `20`; unknown avg `461.1119` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1993`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.196`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1867`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
