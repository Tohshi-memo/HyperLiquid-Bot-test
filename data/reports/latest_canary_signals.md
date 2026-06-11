# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T18:37:51.782866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.7628` n `12`; crypto_alt avg `0.1877` n `228`; crypto_major avg `0.2159` n `8`; equity avg `0.2002` n `74`; fx avg `-0.0137` n `6`; index avg `0.1035` n `23`; metal avg `0.1505` n `18`; unknown avg `0.031` n `556`
- 1h: commodity avg `0.9537` n `12`; crypto_alt avg `0.1458` n `228`; crypto_major avg `0.5391` n `8`; equity avg `0.3632` n `74`; fx avg `-0.0531` n `6`; index avg `0.1947` n `23`; metal avg `0.1396` n `18`; unknown avg `0.3418` n `556`
- 4h: commodity avg `-0.4931` n `12`; crypto_alt avg `1.0586` n `228`; crypto_major avg `1.4143` n `8`; equity avg `1.2287` n `74`; fx avg `0.0163` n `6`; index avg `0.762` n `23`; metal avg `1.7145` n `18`; unknown avg `0.1941` n `556`
- 24h: commodity avg `-0.8473` n `12`; crypto_alt avg `3.165` n `228`; crypto_major avg `3.4505` n `8`; equity avg `1.8232` n `74`; fx avg `-0.0093` n `6`; index avg `1.3029` n `23`; metal avg `1.5174` n `18`; unknown avg `2.4358` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
