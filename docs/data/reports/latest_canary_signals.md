# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T16:31:50.980306+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0253` n `12`; crypto_alt avg `-0.0184` n `233`; crypto_major avg `0.0021` n `8`; equity avg `-0.0096` n `136`; fx avg `-0.0012` n `6`; index avg `-0.0009` n `27`; metal avg `0.0088` n `20`; unknown avg `-0.0782` n `832`
- 1h: commodity avg `0.0222` n `12`; crypto_alt avg `0.1456` n `233`; crypto_major avg `0.2895` n `8`; equity avg `0.1837` n `136`; fx avg `-0.0051` n `6`; index avg `0.0352` n `27`; metal avg `0.0124` n `20`; unknown avg `0.4261` n `830`
- 4h: commodity avg `0.0225` n `12`; crypto_alt avg `0.0726` n `233`; crypto_major avg `0.7347` n `8`; equity avg `0.3723` n `136`; fx avg `0.0059` n `6`; index avg `0.0697` n `27`; metal avg `0.0154` n `20`; unknown avg `1.2982` n `830`
- 24h: commodity avg `0.3095` n `12`; crypto_alt avg `-0.6494` n `233`; crypto_major avg `-1.1889` n `8`; equity avg `-1.576` n `136`; fx avg `0.0087` n `6`; index avg `-0.2602` n `26`; metal avg `-0.0837` n `20`; unknown avg `-0.2677` n `708`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
