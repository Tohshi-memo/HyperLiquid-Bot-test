# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T02:07:27.386230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0372` n `13`; crypto_alt avg `0.2474` n `234`; crypto_major avg `0.2652` n `8`; equity avg `0.0511` n `142`; fx avg `-0.0115` n `6`; index avg `0.0081` n `26`; metal avg `0.0742` n `20`; unknown avg `0.2453` n `983`
- 1h: commodity avg `0.001` n `13`; crypto_alt avg `0.4919` n `234`; crypto_major avg `0.3823` n `8`; equity avg `0.0075` n `142`; fx avg `-0.0427` n `6`; index avg `0.023` n `26`; metal avg `0.016` n `20`; unknown avg `0.5812` n `983`
- 4h: commodity avg `-0.18` n `13`; crypto_alt avg `0.6332` n `234`; crypto_major avg `0.5064` n `8`; equity avg `0.0882` n `142`; fx avg `-0.0215` n `6`; index avg `0.0344` n `26`; metal avg `-0.159` n `20`; unknown avg `0.4289` n `977`
- 24h: commodity avg `0.2208` n `13`; crypto_alt avg `0.2712` n `234`; crypto_major avg `0.4342` n `8`; equity avg `0.841` n `142`; fx avg `-0.2266` n `6`; index avg `0.1277` n `26`; metal avg `-0.1523` n `20`; unknown avg `0.3953` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
