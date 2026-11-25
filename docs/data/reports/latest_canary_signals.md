# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T09:07:31.073149+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0185` n `13`; crypto_alt avg `-0.0273` n `239`; crypto_major avg `-0.2143` n `8`; equity avg `-0.3897` n `168`; fx avg `-0.0075` n `6`; index avg `-0.0482` n `27`; metal avg `0.0233` n `20`; unknown avg `0.2383` n `1253`
- 1h: commodity avg `0.2494` n `13`; crypto_alt avg `0.2209` n `239`; crypto_major avg `0.2993` n `8`; equity avg `-0.0314` n `168`; fx avg `0.0385` n `6`; index avg `0.0107` n `27`; metal avg `0.1484` n `20`; unknown avg `3.3443` n `1253`
- 4h: commodity avg `-0.0779` n `13`; crypto_alt avg `0.0274` n `239`; crypto_major avg `-0.4561` n `8`; equity avg `-1.1052` n `168`; fx avg `0.0059` n `6`; index avg `-0.1033` n `27`; metal avg `-0.082` n `20`; unknown avg `168.2251` n `1203`
- 24h: commodity avg `0.3503` n `13`; crypto_alt avg `-1.7856` n `239`; crypto_major avg `-2.4465` n `8`; equity avg `-4.5739` n `167`; fx avg `0.0993` n `6`; index avg `-0.3964` n `27`; metal avg `-0.7753` n `20`; unknown avg `650.2896` n `1035`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
