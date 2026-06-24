# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T00:07:25.351070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0103` n `12`; crypto_alt avg `0.2065` n `228`; crypto_major avg `0.1326` n `8`; equity avg `0.2511` n `86`; fx avg `0.0132` n `6`; index avg `0.0356` n `23`; metal avg `0.1236` n `20`; unknown avg `0.0566` n `764`
- 1h: commodity avg `-0.0368` n `12`; crypto_alt avg `0.3909` n `228`; crypto_major avg `0.3966` n `8`; equity avg `0.6386` n `86`; fx avg `0.0448` n `6`; index avg `0.1588` n `23`; metal avg `0.1649` n `20`; unknown avg `0.4123` n `764`
- 4h: commodity avg `-0.1479` n `12`; crypto_alt avg `0.1968` n `228`; crypto_major avg `0.3574` n `8`; equity avg `0.3372` n `86`; fx avg `0.0249` n `6`; index avg `0.1307` n `23`; metal avg `0.01` n `20`; unknown avg `0.2343` n `756`
- 24h: commodity avg `-0.4805` n `12`; crypto_alt avg `-1.7644` n `228`; crypto_major avg `-2.6696` n `8`; equity avg `-2.7252` n `86`; fx avg `-0.1865` n `6`; index avg `-0.7459` n `23`; metal avg `-1.0958` n `20`; unknown avg `0.7725` n `588`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
