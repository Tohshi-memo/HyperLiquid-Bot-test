# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T13:37:29.641967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.063` n `13`; crypto_alt avg `-0.0085` n `239`; crypto_major avg `-0.0476` n `8`; equity avg `-0.0229` n `168`; fx avg `0.0077` n `6`; index avg `0.0006` n `27`; metal avg `0.0079` n `20`; unknown avg `0.377` n `1267`
- 1h: commodity avg `0.069` n `13`; crypto_alt avg `-0.0712` n `239`; crypto_major avg `0.0735` n `8`; equity avg `-0.003` n `168`; fx avg `0.0002` n `6`; index avg `-0.0013` n `27`; metal avg `-0.0614` n `20`; unknown avg `0.7195` n `1263`
- 4h: commodity avg `0.2408` n `13`; crypto_alt avg `0.0212` n `239`; crypto_major avg `-0.1373` n `8`; equity avg `0.2738` n `168`; fx avg `0.0076` n `6`; index avg `0.0387` n `27`; metal avg `-0.1172` n `20`; unknown avg `1.8304` n `1249`
- 24h: commodity avg `0.442` n `13`; crypto_alt avg `4.9034` n `239`; crypto_major avg `4.4148` n `8`; equity avg `4.9982` n `168`; fx avg `0.083` n `6`; index avg `0.4962` n `27`; metal avg `0.957` n `20`; unknown avg `115.7574` n `1055`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
