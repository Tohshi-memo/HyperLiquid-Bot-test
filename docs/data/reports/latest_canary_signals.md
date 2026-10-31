# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T20:22:27.096229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `13`; crypto_alt avg `-0.0799` n `238`; crypto_major avg `-0.0517` n `8`; equity avg `-0.0081` n `156`; fx avg `0.0088` n `6`; index avg `-0.0069` n `27`; metal avg `0.0033` n `20`; unknown avg `0.3655` n `1262`
- 1h: commodity avg `-0.0372` n `13`; crypto_alt avg `-0.234` n `238`; crypto_major avg `-0.074` n `8`; equity avg `-0.0355` n `156`; fx avg `0.0112` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0007` n `20`; unknown avg `1.9758` n `1226`
- 4h: commodity avg `0.0027` n `13`; crypto_alt avg `-0.7441` n `238`; crypto_major avg `0.0245` n `8`; equity avg `0.0036` n `156`; fx avg `0.0092` n `6`; index avg `-0.0011` n `27`; metal avg `-0.009` n `20`; unknown avg `0.2815` n `1190`
- 24h: commodity avg `-0.1934` n `13`; crypto_alt avg `0.787` n `238`; crypto_major avg `0.3505` n `8`; equity avg `0.2074` n `156`; fx avg `-0.0035` n `6`; index avg `-0.0503` n `27`; metal avg `0.0771` n `20`; unknown avg `1.7394` n `1091`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
