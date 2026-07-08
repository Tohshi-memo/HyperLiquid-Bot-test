# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T12:37:28.232658+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.067` n `12`; crypto_alt avg `-0.1083` n `229`; crypto_major avg `-0.1542` n `8`; equity avg `0.0881` n `91`; fx avg `-0.0053` n `6`; index avg `0.0294` n `25`; metal avg `-0.0104` n `20`; unknown avg `-0.0793` n `763`
- 1h: commodity avg `-0.2888` n `12`; crypto_alt avg `0.3028` n `229`; crypto_major avg `0.2175` n `8`; equity avg `0.7138` n `91`; fx avg `-0.0093` n `6`; index avg `0.1457` n `25`; metal avg `0.2527` n `20`; unknown avg `0.1936` n `757`
- 4h: commodity avg `-0.343` n `12`; crypto_alt avg `0.5058` n `229`; crypto_major avg `0.6051` n `8`; equity avg `0.7767` n `91`; fx avg `-0.0403` n `6`; index avg `0.1435` n `25`; metal avg `-0.2917` n `20`; unknown avg `0.0828` n `757`
- 24h: commodity avg `1.33` n `12`; crypto_alt avg `-3.5572` n `229`; crypto_major avg `-3.1202` n `8`; equity avg `-2.3724` n `91`; fx avg `-0.0785` n `6`; index avg `-0.5488` n `25`; metal avg `-1.4077` n `20`; unknown avg `-0.6496` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
