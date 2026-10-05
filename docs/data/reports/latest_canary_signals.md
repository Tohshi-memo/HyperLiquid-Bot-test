# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T21:25:28.838799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `13`; crypto_alt avg `0.3671` n `235`; crypto_major avg `0.1408` n `8`; equity avg `0.0542` n `144`; fx avg `0.0118` n `6`; index avg `0.0112` n `26`; metal avg `0.0148` n `20`; unknown avg `2.0345` n `1049`
- 1h: commodity avg `-0.0031` n `13`; crypto_alt avg `0.3671` n `235`; crypto_major avg `0.1408` n `8`; equity avg `0.0542` n `144`; fx avg `0.0118` n `6`; index avg `0.0112` n `26`; metal avg `0.0148` n `20`; unknown avg `2.0345` n `1049`
- 4h: commodity avg `-0.0751` n `13`; crypto_alt avg `1.3301` n `235`; crypto_major avg `0.7037` n `8`; equity avg `0.2245` n `144`; fx avg `0.0253` n `6`; index avg `0.0352` n `26`; metal avg `0.0677` n `20`; unknown avg `2.3185` n `1003`
- 24h: commodity avg `-0.345` n `13`; crypto_alt avg `0.9324` n `235`; crypto_major avg `0.277` n `8`; equity avg `0.3448` n `144`; fx avg `-0.0695` n `6`; index avg `0.1326` n `26`; metal avg `0.1784` n `20`; unknown avg `612.0281` n `818`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1996`, n `671`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1798`, n `671`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.171`, n `671`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1257`, n `671`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `671`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1006`, n `671`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0967`, n `671`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0959`, n `671`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0941`, n `671`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `671`, weak_sample_signal
