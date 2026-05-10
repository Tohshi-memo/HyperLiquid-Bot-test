# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T10:22:19.114145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `0.1572` n `228`; crypto_major avg `0.005` n `8`; equity avg `0.0408` n `65`; fx avg `0.0` n `5`; index avg `0.0014` n `23`; metal avg `0.004` n `18`; unknown avg `-0.1216` n `376`
- 1h: commodity avg `0.0078` n `12`; crypto_alt avg `-0.2746` n `228`; crypto_major avg `-0.2662` n `8`; equity avg `-0.0422` n `65`; fx avg `0.0` n `5`; index avg `0.0149` n `23`; metal avg `0.0052` n `18`; unknown avg `0.104` n `376`
- 4h: commodity avg `-0.1436` n `12`; crypto_alt avg `0.3494` n `228`; crypto_major avg `0.1206` n `8`; equity avg `0.011` n `65`; fx avg `0.0102` n `5`; index avg `-0.0131` n `23`; metal avg `-0.0542` n `18`; unknown avg `-0.1428` n `376`
- 24h: commodity avg `0.0717` n `12`; crypto_alt avg `-0.0942` n `228`; crypto_major avg `-0.0626` n `8`; equity avg `0.9116` n `65`; fx avg `-0.0193` n `5`; index avg `0.2923` n `23`; metal avg `0.4232` n `18`; unknown avg `0.1198` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
