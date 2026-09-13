# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T19:52:27.120858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.0257` n `233`; crypto_major avg `-0.0562` n `8`; equity avg `0.0073` n `136`; fx avg `-0.0085` n `6`; index avg `-0.0028` n `27`; metal avg `0.0038` n `20`; unknown avg `1.0673` n `840`
- 1h: commodity avg `0.0829` n `12`; crypto_alt avg `-0.4915` n `233`; crypto_major avg `-0.2923` n `8`; equity avg `-0.1154` n `136`; fx avg `-0.0055` n `6`; index avg `-0.0238` n `27`; metal avg `-0.0238` n `20`; unknown avg `2.8011` n `838`
- 4h: commodity avg `0.0819` n `12`; crypto_alt avg `0.1633` n `233`; crypto_major avg `0.3399` n `8`; equity avg `0.2447` n `136`; fx avg `-0.0066` n `6`; index avg `0.0041` n `27`; metal avg `0.0204` n `20`; unknown avg `2.1769` n `766`
- 24h: commodity avg `0.3181` n `12`; crypto_alt avg `0.0106` n `233`; crypto_major avg `-0.6365` n `8`; equity avg `-1.2885` n `136`; fx avg `0.0073` n `6`; index avg `-0.2726` n `26`; metal avg `-0.0957` n `20`; unknown avg `2.5887` n `720`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
