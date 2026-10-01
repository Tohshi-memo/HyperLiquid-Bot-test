# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T12:52:29.741090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1113` n `13`; crypto_alt avg `-0.0973` n `234`; crypto_major avg `-0.1908` n `8`; equity avg `-0.1062` n `142`; fx avg `-0.005` n `6`; index avg `-0.0344` n `26`; metal avg `-0.0359` n `20`; unknown avg `1.1141` n `975`
- 1h: commodity avg `0.0718` n `13`; crypto_alt avg `-0.3313` n `234`; crypto_major avg `-0.3689` n `8`; equity avg `-0.189` n `142`; fx avg `-0.0332` n `6`; index avg `-0.038` n `26`; metal avg `0.0274` n `20`; unknown avg `-0.0284` n `967`
- 4h: commodity avg `-0.1126` n `13`; crypto_alt avg `-0.4777` n `234`; crypto_major avg `0.2978` n `8`; equity avg `0.0279` n `142`; fx avg `-0.0168` n `6`; index avg `0.0849` n `26`; metal avg `0.3174` n `20`; unknown avg `5.3654` n `967`
- 24h: commodity avg `-0.0681` n `13`; crypto_alt avg `-2.1994` n `234`; crypto_major avg `-1.5365` n `8`; equity avg `-0.2537` n `142`; fx avg `0.0528` n `6`; index avg `0.0542` n `26`; metal avg `-0.1778` n `20`; unknown avg `775.5823` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
