# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T10:21:57.672890+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1092` n `13`; crypto_alt avg `-0.2672` n `237`; crypto_major avg `-0.1128` n `8`; equity avg `-0.2336` n `151`; fx avg `-0.0019` n `6`; index avg `-0.0385` n `26`; metal avg `-0.0741` n `20`; unknown avg `1.1588` n `1198`
- 1h: commodity avg `0.1092` n `13`; crypto_alt avg `-0.2672` n `237`; crypto_major avg `-0.1128` n `8`; equity avg `-0.2336` n `151`; fx avg `-0.0019` n `6`; index avg `-0.0385` n `26`; metal avg `-0.0741` n `20`; unknown avg `1.1588` n `1198`
- 4h: commodity avg `0.0142` n `13`; crypto_alt avg `0.2382` n `237`; crypto_major avg `0.4321` n `8`; equity avg `-0.5145` n `151`; fx avg `0.0162` n `6`; index avg `-0.0629` n `26`; metal avg `-0.0081` n `20`; unknown avg `3.6255` n `1176`
- 24h: commodity avg `-0.1748` n `13`; crypto_alt avg `3.3794` n `237`; crypto_major avg `2.4619` n `8`; equity avg `2.3574` n `151`; fx avg `0.0238` n `6`; index avg `0.291` n `26`; metal avg `-0.1597` n `20`; unknown avg `5293.1439` n `986`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1676`, n `671`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1444`, n `671`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1225`, n `671`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1223`, n `671`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1183`, n `671`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `671`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1044`, n `671`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1013`, n `671`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.09`, n `671`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0891`, n `671`, weak_sample_signal
