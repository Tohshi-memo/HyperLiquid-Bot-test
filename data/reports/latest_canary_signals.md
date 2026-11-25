# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T04:37:27.578800+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `13`; crypto_alt avg `-0.2776` n `239`; crypto_major avg `-0.2198` n `8`; equity avg `-0.2917` n `168`; fx avg `-0.0128` n `6`; index avg `-0.029` n `27`; metal avg `-0.0706` n `20`; unknown avg `2.1947` n `1265`
- 1h: commodity avg `0.0491` n `13`; crypto_alt avg `0.0336` n `239`; crypto_major avg `-0.4328` n `8`; equity avg `-0.4277` n `168`; fx avg `-0.0318` n `6`; index avg `-0.0238` n `27`; metal avg `-0.0586` n `20`; unknown avg `4.0259` n `1249`
- 4h: commodity avg `-0.2405` n `13`; crypto_alt avg `0.1751` n `239`; crypto_major avg `-0.7258` n `8`; equity avg `-0.7493` n `168`; fx avg `-0.0792` n `6`; index avg `-0.0462` n `27`; metal avg `-0.0692` n `20`; unknown avg `25.4149` n `1245`
- 24h: commodity avg `0.5382` n `13`; crypto_alt avg `-3.2035` n `239`; crypto_major avg `-3.3773` n `8`; equity avg `-5.1585` n `167`; fx avg `0.1615` n `6`; index avg `-0.5042` n `27`; metal avg `-0.9011` n `20`; unknown avg `503.1074` n `1029`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
