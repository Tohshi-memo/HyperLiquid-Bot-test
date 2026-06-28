# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T13:52:28.033039+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.0464` n `228`; crypto_major avg `-0.053` n `8`; equity avg `0.0387` n `88`; fx avg `-0.0015` n `6`; index avg `0.0015` n `23`; metal avg `0.0062` n `20`; unknown avg `-0.0421` n `764`
- 1h: commodity avg `0.0544` n `12`; crypto_alt avg `-0.1974` n `228`; crypto_major avg `-0.1273` n `8`; equity avg `0.0398` n `88`; fx avg `-0.0065` n `6`; index avg `0.0068` n `23`; metal avg `-0.0197` n `20`; unknown avg `-0.1002` n `764`
- 4h: commodity avg `0.0684` n `12`; crypto_alt avg `-0.0472` n `228`; crypto_major avg `0.0098` n `8`; equity avg `0.0339` n `88`; fx avg `0.0035` n `6`; index avg `0.0125` n `23`; metal avg `-0.0138` n `20`; unknown avg `-0.5491` n `764`
- 24h: commodity avg `0.1279` n `12`; crypto_alt avg `-0.6031` n `228`; crypto_major avg `-1.1292` n `8`; equity avg `0.0313` n `88`; fx avg `-0.0038` n `6`; index avg `-0.0313` n `23`; metal avg `-0.0442` n `20`; unknown avg `15.4455` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2008`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
