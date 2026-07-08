# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T00:52:24.829219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0229` n `12`; crypto_alt avg `0.0804` n `229`; crypto_major avg `-0.0154` n `8`; equity avg `0.5465` n `91`; fx avg `-0.0161` n `6`; index avg `0.1156` n `25`; metal avg `0.0743` n `20`; unknown avg `-0.0444` n `763`
- 1h: commodity avg `-0.058` n `12`; crypto_alt avg `0.4565` n `229`; crypto_major avg `0.14` n `8`; equity avg `1.3466` n `91`; fx avg `-0.0353` n `6`; index avg `0.2604` n `25`; metal avg `0.1643` n `20`; unknown avg `0.3114` n `763`
- 4h: commodity avg `-0.017` n `12`; crypto_alt avg `-0.0981` n `229`; crypto_major avg `-0.3035` n `8`; equity avg `0.6407` n `91`; fx avg `0.0401` n `6`; index avg `0.1651` n `25`; metal avg `0.0769` n `20`; unknown avg `-0.1243` n `763`
- 24h: commodity avg `0.8375` n `12`; crypto_alt avg `-2.4273` n `229`; crypto_major avg `-1.9251` n `8`; equity avg `-1.8548` n `91`; fx avg `-0.2135` n `6`; index avg `-0.2374` n `25`; metal avg `-0.3664` n `20`; unknown avg `-0.2034` n `729`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
