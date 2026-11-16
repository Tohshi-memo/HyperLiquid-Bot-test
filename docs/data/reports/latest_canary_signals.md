# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T19:50:13.406546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `13`; crypto_alt avg `0.0371` n `239`; crypto_major avg `0.0875` n `8`; equity avg `-0.24` n `162`; fx avg `0.0085` n `6`; index avg `-0.0348` n `27`; metal avg `-0.0147` n `20`; unknown avg `161.2308` n `1266`
- 1h: commodity avg `0.0155` n `13`; crypto_alt avg `-0.3169` n `239`; crypto_major avg `-0.2662` n `8`; equity avg `-0.2924` n `162`; fx avg `0.0217` n `6`; index avg `-0.0623` n `27`; metal avg `0.0324` n `20`; unknown avg `3.1183` n `1264`
- 4h: commodity avg `-0.4223` n `13`; crypto_alt avg `0.3114` n `239`; crypto_major avg `0.3833` n `8`; equity avg `-0.7243` n `162`; fx avg `-0.0072` n `6`; index avg `-0.136` n `27`; metal avg `-0.0505` n `20`; unknown avg `3.8405` n `1249`
- 24h: commodity avg `-1.135` n `13`; crypto_alt avg `-0.1368` n `239`; crypto_major avg `-0.105` n `8`; equity avg `-3.0696` n `162`; fx avg `-0.0977` n `6`; index avg `-0.3151` n `27`; metal avg `-0.2735` n `20`; unknown avg `252.6007` n `1037`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.136`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1258`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1192`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1095`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1033`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1005`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0951`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0875`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `669`, weak_sample_signal
