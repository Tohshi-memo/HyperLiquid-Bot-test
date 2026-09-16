# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T00:22:30.785480+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0594` n `12`; crypto_alt avg `-0.0294` n `234`; crypto_major avg `0.0699` n `8`; equity avg `0.0823` n `137`; fx avg `0.0092` n `6`; index avg `0.0159` n `27`; metal avg `-0.0016` n `20`; unknown avg `0.4749` n `919`
- 1h: commodity avg `-0.1019` n `12`; crypto_alt avg `-0.3101` n `234`; crypto_major avg `-0.3714` n `8`; equity avg `0.0542` n `137`; fx avg `0.0357` n `6`; index avg `0.0186` n `27`; metal avg `-0.0173` n `20`; unknown avg `-0.1389` n `917`
- 4h: commodity avg `-0.119` n `12`; crypto_alt avg `-0.0637` n `234`; crypto_major avg `0.0475` n `8`; equity avg `0.0162` n `137`; fx avg `0.031` n `6`; index avg `0.0137` n `27`; metal avg `-0.0103` n `20`; unknown avg `0.1886` n `861`
- 24h: commodity avg `0.2892` n `12`; crypto_alt avg `-3.6724` n `234`; crypto_major avg `-3.8446` n `8`; equity avg `-1.3476` n `137`; fx avg `0.2339` n `6`; index avg `-0.1257` n `27`; metal avg `0.2854` n `20`; unknown avg `0.7127` n `802`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
