# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T09:22:25.353074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.138` n `12`; crypto_alt avg `0.1351` n `230`; crypto_major avg `0.2372` n `8`; equity avg `0.0543` n `93`; fx avg `0.0022` n `6`; index avg `0.0044` n `25`; metal avg `-0.0349` n `20`; unknown avg `0.0` n `767`
- 1h: commodity avg `-0.0362` n `12`; crypto_alt avg `0.3822` n `230`; crypto_major avg `0.5887` n `8`; equity avg `0.3417` n `93`; fx avg `-0.0205` n `6`; index avg `0.0459` n `25`; metal avg `0.0577` n `20`; unknown avg `0.0541` n `767`
- 4h: commodity avg `0.0423` n `12`; crypto_alt avg `0.3409` n `230`; crypto_major avg `0.5942` n `8`; equity avg `0.0221` n `93`; fx avg `-0.001` n `6`; index avg `-0.0379` n `25`; metal avg `0.071` n `20`; unknown avg `-0.0474` n `747`
- 24h: commodity avg `-0.0796` n `12`; crypto_alt avg `1.7479` n `230`; crypto_major avg `3.4427` n `8`; equity avg `1.2805` n `92`; fx avg `0.0225` n `6`; index avg `0.4449` n `25`; metal avg `0.2986` n `20`; unknown avg `0.313` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
