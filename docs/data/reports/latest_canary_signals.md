# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T17:52:25.905104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0045` n `12`; crypto_alt avg `0.1135` n `232`; crypto_major avg `0.1774` n `8`; equity avg `0.0293` n `134`; fx avg `0.0022` n `6`; index avg `0.0008` n `26`; metal avg `0.0008` n `20`; unknown avg `-0.2023` n `796`
- 1h: commodity avg `0.0247` n `12`; crypto_alt avg `0.0759` n `232`; crypto_major avg `0.2154` n `8`; equity avg `0.1699` n `134`; fx avg `-0.005` n `6`; index avg `0.0281` n `26`; metal avg `-0.0077` n `20`; unknown avg `-0.1842` n `794`
- 4h: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.7175` n `232`; crypto_major avg `-0.6302` n `8`; equity avg `0.0972` n `134`; fx avg `-0.0366` n `6`; index avg `0.0404` n `26`; metal avg `0.0863` n `20`; unknown avg `-0.4688` n `788`
- 24h: commodity avg `0.1589` n `12`; crypto_alt avg `0.4628` n `232`; crypto_major avg `-0.7317` n `8`; equity avg `0.5125` n `134`; fx avg `-0.1183` n `6`; index avg `0.0889` n `26`; metal avg `0.0077` n `20`; unknown avg `147.647` n `681`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
