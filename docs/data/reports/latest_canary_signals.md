# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T15:22:36.879444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.091` n `13`; crypto_alt avg `0.5826` n `234`; crypto_major avg `0.3449` n `8`; equity avg `0.2104` n `142`; fx avg `-0.0259` n `6`; index avg `0.0476` n `26`; metal avg `0.0623` n `20`; unknown avg `0.2851` n `965`
- 1h: commodity avg `0.202` n `13`; crypto_alt avg `0.3095` n `234`; crypto_major avg `0.1371` n `8`; equity avg `0.3961` n `142`; fx avg `-0.0866` n `6`; index avg `0.0486` n `26`; metal avg `0.0302` n `20`; unknown avg `0.0326` n `915`
- 4h: commodity avg `0.2541` n `13`; crypto_alt avg `-0.4301` n `234`; crypto_major avg `-0.1831` n `8`; equity avg `-0.5805` n `142`; fx avg `-0.1327` n `6`; index avg `-0.1689` n `26`; metal avg `-0.0681` n `20`; unknown avg `0.9793` n `909`
- 24h: commodity avg `-0.1423` n `13`; crypto_alt avg `-0.8729` n `234`; crypto_major avg `0.2957` n `8`; equity avg `-0.0799` n `142`; fx avg `-0.0975` n `6`; index avg `-0.113` n `26`; metal avg `-0.094` n `20`; unknown avg `3.1608` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
