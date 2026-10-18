# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T19:37:27.701761+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `13`; crypto_alt avg `-0.67` n `237`; crypto_major avg `-0.3902` n `8`; equity avg `-0.0962` n `151`; fx avg `0.0` n `6`; index avg `-0.0149` n `26`; metal avg `-0.0222` n `20`; unknown avg `10.9232` n `1200`
- 1h: commodity avg `0.0085` n `13`; crypto_alt avg `-1.214` n `237`; crypto_major avg `-0.6579` n `8`; equity avg `-0.1665` n `151`; fx avg `-0.0061` n `6`; index avg `-0.008` n `26`; metal avg `-0.018` n `20`; unknown avg `5.2097` n `1184`
- 4h: commodity avg `0.0035` n `13`; crypto_alt avg `-1.5726` n `237`; crypto_major avg `-0.7915` n `8`; equity avg `-0.2709` n `151`; fx avg `0.0057` n `6`; index avg `-0.0164` n `26`; metal avg `-0.0136` n `20`; unknown avg `-0.0697` n `1144`
- 24h: commodity avg `-0.021` n `13`; crypto_alt avg `-4.9298` n `236`; crypto_major avg `-2.2411` n `8`; equity avg `-1.2661` n `151`; fx avg `-0.0002` n `6`; index avg `-0.159` n `26`; metal avg `-0.0719` n `20`; unknown avg `0.726` n `1007`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2104`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1402`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1365`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0804`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0636`, n `666`, weak_sample_signal
