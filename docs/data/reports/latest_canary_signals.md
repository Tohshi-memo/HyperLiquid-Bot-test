# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T07:07:27.506389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0415` n `12`; crypto_alt avg `0.0304` n `229`; crypto_major avg `0.0648` n `8`; equity avg `0.0536` n `91`; fx avg `0.009` n `6`; index avg `0.0027` n `25`; metal avg `-0.0407` n `20`; unknown avg `-0.0142` n `763`
- 1h: commodity avg `0.0793` n `12`; crypto_alt avg `0.4446` n `229`; crypto_major avg `0.5721` n `8`; equity avg `0.2227` n `91`; fx avg `0.0142` n `6`; index avg `0.0139` n `25`; metal avg `0.0371` n `20`; unknown avg `0.2986` n `763`
- 4h: commodity avg `0.1876` n `12`; crypto_alt avg `-0.0349` n `229`; crypto_major avg `0.0454` n `8`; equity avg `-0.0858` n `91`; fx avg `0.0296` n `6`; index avg `-0.0673` n `25`; metal avg `-0.2035` n `20`; unknown avg `13.0798` n `745`
- 24h: commodity avg `0.3539` n `12`; crypto_alt avg `0.8228` n `229`; crypto_major avg `0.0412` n `8`; equity avg `-1.2318` n `90`; fx avg `-0.0015` n `6`; index avg `-0.322` n `25`; metal avg `-0.3126` n `20`; unknown avg `-0.3277` n `743`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
