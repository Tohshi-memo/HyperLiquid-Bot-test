# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T10:37:29.790831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0408` n `12`; crypto_alt avg `-0.0743` n `228`; crypto_major avg `-0.0194` n `8`; equity avg `0.0173` n `86`; fx avg `-0.0077` n `6`; index avg `0.0056` n `23`; metal avg `0.0091` n `20`; unknown avg `-0.0366` n `764`
- 1h: commodity avg `0.0256` n `12`; crypto_alt avg `-0.3625` n `228`; crypto_major avg `-0.1775` n `8`; equity avg `0.052` n `86`; fx avg `-0.0477` n `6`; index avg `0.0319` n `23`; metal avg `-0.1908` n `20`; unknown avg `-0.0826` n `764`
- 4h: commodity avg `-0.0601` n `12`; crypto_alt avg `-0.5386` n `228`; crypto_major avg `-0.6931` n `8`; equity avg `-0.1423` n `86`; fx avg `-0.0445` n `6`; index avg `0.0252` n `23`; metal avg `-0.5174` n `20`; unknown avg `-0.434` n `756`
- 24h: commodity avg `-0.5261` n `12`; crypto_alt avg `0.0128` n `228`; crypto_major avg `0.0443` n `8`; equity avg `5.0216` n `86`; fx avg `-0.0307` n `6`; index avg `0.1613` n `23`; metal avg `-0.7466` n `20`; unknown avg `-0.0547` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
