# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T00:22:24.278670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `-0.0662` n `229`; crypto_major avg `-0.1619` n `8`; equity avg `0.015` n `88`; fx avg `0.0` n `6`; index avg `0.0011` n `25`; metal avg `-0.0043` n `20`; unknown avg `-0.1216` n `765`
- 1h: commodity avg `-0.0334` n `12`; crypto_alt avg `-0.218` n `229`; crypto_major avg `-0.3285` n `8`; equity avg `-0.0106` n `88`; fx avg `-0.001` n `6`; index avg `-0.0085` n `25`; metal avg `-0.0025` n `20`; unknown avg `-0.3287` n `765`
- 4h: commodity avg `-0.0074` n `12`; crypto_alt avg `-0.5282` n `229`; crypto_major avg `-0.4346` n `8`; equity avg `0.0484` n `88`; fx avg `0.0241` n `6`; index avg `0.0058` n `25`; metal avg `0.0326` n `20`; unknown avg `-0.1101` n `765`
- 24h: commodity avg `-0.028` n `12`; crypto_alt avg `-0.3107` n `229`; crypto_major avg `-0.1209` n `8`; equity avg `0.25` n `88`; fx avg `-0.0139` n `6`; index avg `0.019` n `25`; metal avg `0.0921` n `20`; unknown avg `-0.8175` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
