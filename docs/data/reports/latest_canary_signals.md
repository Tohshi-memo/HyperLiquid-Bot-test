# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T23:37:30.272668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `-0.4103` n `234`; crypto_major avg `-0.5069` n `8`; equity avg `-0.0434` n `137`; fx avg `0.0014` n `6`; index avg `-0.0018` n `27`; metal avg `-0.004` n `20`; unknown avg `0.4768` n `919`
- 1h: commodity avg `0.0346` n `12`; crypto_alt avg `0.2236` n `234`; crypto_major avg `0.0251` n `8`; equity avg `-0.0309` n `137`; fx avg `0.0032` n `6`; index avg `-0.0084` n `27`; metal avg `-0.0543` n `20`; unknown avg `-0.1239` n `917`
- 4h: commodity avg `0.0116` n `12`; crypto_alt avg `-0.5715` n `234`; crypto_major avg `-0.375` n `8`; equity avg `-0.0573` n `137`; fx avg `-0.005` n `6`; index avg `0.0473` n `27`; metal avg `-0.0182` n `20`; unknown avg `0.5967` n `845`
- 24h: commodity avg `0.4625` n `12`; crypto_alt avg `-3.7628` n `234`; crypto_major avg `-4.0804` n `8`; equity avg `-1.3337` n `137`; fx avg `0.2303` n `6`; index avg `-0.0764` n `27`; metal avg `0.2046` n `20`; unknown avg `0.9788` n `802`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
