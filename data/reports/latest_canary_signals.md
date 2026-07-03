# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T22:32:02.638575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `-0.0447` n `229`; crypto_major avg `-0.088` n `8`; equity avg `-0.0434` n `88`; fx avg `-0.0004` n `6`; index avg `-0.0006` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.0178` n `765`
- 1h: commodity avg `0.0256` n `12`; crypto_alt avg `0.0421` n `229`; crypto_major avg `-0.0159` n `8`; equity avg `-0.066` n `88`; fx avg `0.024` n `6`; index avg `-0.0075` n `25`; metal avg `-0.024` n `20`; unknown avg `-0.0155` n `765`
- 4h: commodity avg `-0.0168` n `12`; crypto_alt avg `0.5756` n `229`; crypto_major avg `0.587` n `8`; equity avg `-0.0342` n `88`; fx avg `-0.0143` n `6`; index avg `-0.0466` n `25`; metal avg `-0.0107` n `20`; unknown avg `-0.3117` n `765`
- 24h: commodity avg `0.1393` n `12`; crypto_alt avg `3.3392` n `229`; crypto_major avg `3.3668` n `8`; equity avg `1.7092` n `88`; fx avg `-0.0644` n `6`; index avg `0.4429` n `25`; metal avg `0.509` n `20`; unknown avg `5.165` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
