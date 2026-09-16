# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T02:07:29.519352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0298` n `12`; crypto_alt avg `0.0368` n `234`; crypto_major avg `0.0743` n `8`; equity avg `0.0396` n `137`; fx avg `-0.0051` n `6`; index avg `0.0072` n `27`; metal avg `-0.0053` n `20`; unknown avg `0.1891` n `917`
- 1h: commodity avg `0.0221` n `12`; crypto_alt avg `-0.5995` n `234`; crypto_major avg `-0.3321` n `8`; equity avg `-0.0519` n `137`; fx avg `0.0197` n `6`; index avg `-0.0018` n `27`; metal avg `0.0128` n `20`; unknown avg `-0.0296` n `917`
- 4h: commodity avg `-0.0126` n `12`; crypto_alt avg `-0.3532` n `234`; crypto_major avg `-0.0124` n `8`; equity avg `-0.0604` n `137`; fx avg `0.1302` n `6`; index avg `-0.0036` n `27`; metal avg `-0.063` n `20`; unknown avg `-0.2094` n `903`
- 24h: commodity avg `0.3283` n `12`; crypto_alt avg `-4.4069` n `234`; crypto_major avg `-4.2383` n `8`; equity avg `-1.6295` n `137`; fx avg `0.274` n `6`; index avg `-0.1633` n `27`; metal avg `0.0794` n `20`; unknown avg `0.4943` n `802`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
