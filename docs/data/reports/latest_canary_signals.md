# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T21:07:27.151602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `0.0428` n `233`; crypto_major avg `0.0767` n `8`; equity avg `-0.0111` n `136`; fx avg `-0.0005` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0156` n `20`; unknown avg `0.4041` n `836`
- 1h: commodity avg `-0.0156` n `12`; crypto_alt avg `0.0679` n `233`; crypto_major avg `0.0481` n `8`; equity avg `-0.0471` n `136`; fx avg `-0.0045` n `6`; index avg `-0.0083` n `26`; metal avg `-0.0225` n `20`; unknown avg `19.8063` n `830`
- 4h: commodity avg `0.034` n `12`; crypto_alt avg `-0.3058` n `233`; crypto_major avg `-0.3479` n `8`; equity avg `-0.3167` n `136`; fx avg `-0.0073` n `6`; index avg `-0.0325` n `26`; metal avg `-0.0317` n `20`; unknown avg `6.9615` n `790`
- 24h: commodity avg `-0.0948` n `12`; crypto_alt avg `0.9715` n `233`; crypto_major avg `-0.2573` n `8`; equity avg `-0.2999` n `136`; fx avg `-0.0216` n `6`; index avg `0.0187` n `26`; metal avg `-0.0285` n `20`; unknown avg `1.9211` n `736`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0487`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0454`, n `668`, weak_sample_signal
