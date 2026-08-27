# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T04:37:31.076317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0225` n `12`; crypto_alt avg `-0.2141` n `231`; crypto_major avg `-0.2605` n `8`; equity avg `-0.1195` n `126`; fx avg `-0.0013` n `6`; index avg `-0.0268` n `25`; metal avg `-0.0369` n `20`; unknown avg `-0.0048` n `793`
- 1h: commodity avg `-0.0149` n `12`; crypto_alt avg `-0.4117` n `231`; crypto_major avg `-0.431` n `8`; equity avg `-0.1923` n `126`; fx avg `-0.0029` n `6`; index avg `-0.0445` n `25`; metal avg `-0.1139` n `20`; unknown avg `-0.3707` n `793`
- 4h: commodity avg `0.0588` n `12`; crypto_alt avg `-0.6748` n `231`; crypto_major avg `-0.3838` n `8`; equity avg `0.1445` n `126`; fx avg `0.0142` n `6`; index avg `-0.0114` n `25`; metal avg `0.0231` n `20`; unknown avg `-0.0129` n `793`
- 24h: commodity avg `0.4577` n `12`; crypto_alt avg `-0.2086` n `231`; crypto_major avg `-0.0361` n `8`; equity avg `0.9942` n `126`; fx avg `-0.0991` n `6`; index avg `0.1251` n `25`; metal avg `-0.2781` n `20`; unknown avg `0.2239` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
