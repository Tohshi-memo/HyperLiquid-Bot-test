# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T03:52:38.728548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `13`; crypto_alt avg `0.06` n `234`; crypto_major avg `0.1301` n `8`; equity avg `-0.0158` n `142`; fx avg `0.0037` n `6`; index avg `-0.0065` n `26`; metal avg `-0.0059` n `20`; unknown avg `0.9797` n `985`
- 1h: commodity avg `0.0146` n `13`; crypto_alt avg `-0.1555` n `234`; crypto_major avg `0.168` n `8`; equity avg `0.0095` n `142`; fx avg `0.0059` n `6`; index avg `0.0013` n `26`; metal avg `0.0709` n `20`; unknown avg `0.3528` n `983`
- 4h: commodity avg `-0.1231` n `13`; crypto_alt avg `0.5308` n `234`; crypto_major avg `0.6689` n `8`; equity avg `0.0812` n `142`; fx avg `-0.0031` n `6`; index avg `0.0516` n `26`; metal avg `-0.0746` n `20`; unknown avg `0.8191` n `977`
- 24h: commodity avg `0.7184` n `13`; crypto_alt avg `-0.8963` n `234`; crypto_major avg `0.4623` n `8`; equity avg `0.4857` n `142`; fx avg `-0.2137` n `6`; index avg `0.0465` n `26`; metal avg `-0.1229` n `20`; unknown avg `0.3305` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
