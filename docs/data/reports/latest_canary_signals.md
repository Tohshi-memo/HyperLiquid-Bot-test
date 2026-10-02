# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T14:22:30.295006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.75` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1188` n `13`; crypto_alt avg `0.2885` n `235`; crypto_major avg `0.2728` n `8`; equity avg `0.0721` n `143`; fx avg `-0.0178` n `6`; index avg `0.012` n `26`; metal avg `-0.0506` n `20`; unknown avg `-0.1544` n `984`
- 1h: commodity avg `-0.2585` n `13`; crypto_alt avg `0.0712` n `235`; crypto_major avg `-0.2622` n `8`; equity avg `0.3274` n `143`; fx avg `0.0609` n `6`; index avg `0.0635` n `26`; metal avg `0.0273` n `20`; unknown avg `0.0897` n `952`
- 4h: commodity avg `-0.1491` n `13`; crypto_alt avg `0.8341` n `235`; crypto_major avg `0.1106` n `8`; equity avg `0.9072` n `142`; fx avg `0.0341` n `6`; index avg `0.2647` n `26`; metal avg `0.1417` n `20`; unknown avg `0.8565` n `946`
- 24h: commodity avg `-0.7812` n `13`; crypto_alt avg `3.5152` n `235`; crypto_major avg `2.3699` n `8`; equity avg `3.0201` n `142`; fx avg `-0.2519` n `6`; index avg `0.6821` n `26`; metal avg `0.2266` n `20`; unknown avg `109.6715` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1713`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
