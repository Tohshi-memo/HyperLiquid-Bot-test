# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T03:52:28.685196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `-0.018` n `234`; crypto_major avg `-0.0053` n `8`; equity avg `0.1484` n `137`; fx avg `-0.0001` n `6`; index avg `0.0258` n `27`; metal avg `0.0075` n `20`; unknown avg `0.0753` n `919`
- 1h: commodity avg `-0.0049` n `12`; crypto_alt avg `-0.0543` n `234`; crypto_major avg `-0.0913` n `8`; equity avg `0.4016` n `137`; fx avg `0.0084` n `6`; index avg `0.055` n `27`; metal avg `0.0697` n `20`; unknown avg `0.1726` n `917`
- 4h: commodity avg `-0.1418` n `12`; crypto_alt avg `-0.3371` n `234`; crypto_major avg `0.1907` n `8`; equity avg `0.6738` n `137`; fx avg `0.0504` n `6`; index avg `0.0822` n `27`; metal avg `0.2688` n `20`; unknown avg `0.3101` n `907`
- 24h: commodity avg `0.2354` n `12`; crypto_alt avg `-3.5536` n `234`; crypto_major avg `-3.4205` n `8`; equity avg `-0.7097` n `137`; fx avg `0.2336` n `6`; index avg `-0.046` n `27`; metal avg `0.3353` n `20`; unknown avg `18796.5405` n `802`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
