# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T19:37:31.686171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0388` n `12`; crypto_alt avg `0.0057` n `229`; crypto_major avg `0.1475` n `8`; equity avg `0.1713` n `91`; fx avg `-0.0046` n `6`; index avg `0.0106` n `25`; metal avg `0.0048` n `20`; unknown avg `0.0175` n `764`
- 1h: commodity avg `0.0374` n `12`; crypto_alt avg `0.2024` n `229`; crypto_major avg `0.381` n `8`; equity avg `0.3313` n `91`; fx avg `-0.0125` n `6`; index avg `0.0523` n `25`; metal avg `0.0964` n `20`; unknown avg `1.457` n `764`
- 4h: commodity avg `-0.4765` n `12`; crypto_alt avg `0.6355` n `229`; crypto_major avg `0.8209` n `8`; equity avg `1.2703` n `91`; fx avg `-0.0156` n `6`; index avg `0.3126` n `25`; metal avg `0.551` n `20`; unknown avg `1.4888` n `764`
- 24h: commodity avg `0.3123` n `12`; crypto_alt avg `-2.2763` n `229`; crypto_major avg `-2.8606` n `8`; equity avg `1.0858` n `91`; fx avg `0.0019` n `6`; index avg `0.0077` n `25`; metal avg `-0.7128` n `20`; unknown avg `0.1985` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0481`, n `668`, weak_sample_signal
