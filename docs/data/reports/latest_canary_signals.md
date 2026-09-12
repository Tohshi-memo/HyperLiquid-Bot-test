# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T17:07:28.582635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `0.0334` n `233`; crypto_major avg `0.0251` n `8`; equity avg `-0.0069` n `136`; fx avg `0.0033` n `6`; index avg `-0.0126` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.6944` n `796`
- 1h: commodity avg `0.0319` n `12`; crypto_alt avg `-0.0851` n `233`; crypto_major avg `-0.0145` n `8`; equity avg `0.0225` n `136`; fx avg `0.0028` n `6`; index avg `-0.005` n `26`; metal avg `0.0041` n `20`; unknown avg `0.5253` n `790`
- 4h: commodity avg `0.0052` n `12`; crypto_alt avg `0.2383` n `233`; crypto_major avg `-0.1327` n `8`; equity avg `0.0114` n `136`; fx avg `-0.0068` n `6`; index avg `0.0082` n `26`; metal avg `0.0188` n `20`; unknown avg `0.3574` n `790`
- 24h: commodity avg `-0.1599` n `12`; crypto_alt avg `0.1375` n `233`; crypto_major avg `-0.6997` n `8`; equity avg `-0.2719` n `136`; fx avg `-0.0213` n `6`; index avg `-0.002` n `26`; metal avg `-0.0373` n `20`; unknown avg `10.2296` n `654`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0457`, n `668`, weak_sample_signal
