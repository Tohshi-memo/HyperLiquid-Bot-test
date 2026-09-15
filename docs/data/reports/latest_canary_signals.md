# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T23:52:27.540854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `12`; crypto_alt avg `0.0631` n `234`; crypto_major avg `0.0488` n `8`; equity avg `0.0258` n `137`; fx avg `0.0271` n `6`; index avg `0.0197` n `27`; metal avg `-0.011` n `20`; unknown avg `0.8386` n `919`
- 1h: commodity avg `0.0205` n `12`; crypto_alt avg `0.0227` n `234`; crypto_major avg `-0.0726` n `8`; equity avg `-0.012` n `137`; fx avg `0.0332` n `6`; index avg `0.0038` n `27`; metal avg `-0.0366` n `20`; unknown avg `0.4603` n `917`
- 4h: commodity avg `-0.0075` n `12`; crypto_alt avg `-0.539` n `234`; crypto_major avg `-0.47` n `8`; equity avg `0.0387` n `137`; fx avg `0.0346` n `6`; index avg `0.0522` n `27`; metal avg `-0.0119` n `20`; unknown avg `0.8178` n `845`
- 24h: commodity avg `0.4777` n `12`; crypto_alt avg `-3.6496` n `234`; crypto_major avg `-3.9716` n `8`; equity avg `-1.2768` n `137`; fx avg `0.2508` n `6`; index avg `-0.0652` n `27`; metal avg `0.2179` n `20`; unknown avg `1.5724` n `802`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
