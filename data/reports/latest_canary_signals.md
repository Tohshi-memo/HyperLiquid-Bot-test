# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T19:07:30.770568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `12`; crypto_alt avg `-0.1131` n `229`; crypto_major avg `-0.1254` n `8`; equity avg `0.0416` n `91`; fx avg `-0.0128` n `6`; index avg `0.0052` n `25`; metal avg `-0.0135` n `20`; unknown avg `0.1043` n `764`
- 1h: commodity avg `0.0173` n `12`; crypto_alt avg `0.0025` n `229`; crypto_major avg `-0.1657` n `8`; equity avg `0.156` n `91`; fx avg `-0.0414` n `6`; index avg `0.0176` n `25`; metal avg `0.1695` n `20`; unknown avg `-0.0504` n `764`
- 4h: commodity avg `-0.5716` n `12`; crypto_alt avg `0.537` n `229`; crypto_major avg `0.4584` n `8`; equity avg `0.8386` n `91`; fx avg `-0.0166` n `6`; index avg `0.2247` n `25`; metal avg `0.3932` n `20`; unknown avg `0.0814` n `764`
- 24h: commodity avg `0.3664` n `12`; crypto_alt avg `-2.1016` n `229`; crypto_major avg `-2.7652` n `8`; equity avg `0.8556` n `91`; fx avg `-0.0058` n `6`; index avg `-0.0326` n `25`; metal avg `-0.6812` n `20`; unknown avg `-0.3738` n `737`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
