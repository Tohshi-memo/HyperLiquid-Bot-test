# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T14:37:31.591680+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3617` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0981` n `12`; crypto_alt avg `-0.6767` n `228`; crypto_major avg `-0.4936` n `8`; equity avg `-0.1528` n `74`; fx avg `-0.0012` n `6`; index avg `0.0277` n `23`; metal avg `-0.0168` n `18`; unknown avg `-0.1532` n `645`
- 1h: commodity avg `0.2566` n `12`; crypto_alt avg `-0.617` n `228`; crypto_major avg `-0.6496` n `8`; equity avg `-0.2597` n `74`; fx avg `-0.0037` n `6`; index avg `-0.0133` n `23`; metal avg `-0.0633` n `18`; unknown avg `-0.1157` n `645`
- 4h: commodity avg `0.5245` n `12`; crypto_alt avg `-1.568` n `228`; crypto_major avg `-1.3201` n `8`; equity avg `-0.5591` n `74`; fx avg `-0.0031` n `6`; index avg `0.0416` n `23`; metal avg `-0.208` n `18`; unknown avg `0.2884` n `645`
- 24h: commodity avg `-0.0044` n `12`; crypto_alt avg `-1.4378` n `228`; crypto_major avg `-1.025` n `8`; equity avg `0.2692` n `74`; fx avg `0.0001` n `6`; index avg `0.1317` n `23`; metal avg `0.0125` n `18`; unknown avg `-1.2815` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
