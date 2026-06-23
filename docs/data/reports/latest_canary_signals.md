# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T10:52:28.179892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.651` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5385` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.0566` n `228`; crypto_major avg `-0.0173` n `8`; equity avg `-0.0032` n `86`; fx avg `0.0064` n `6`; index avg `-0.0058` n `23`; metal avg `-0.0283` n `20`; unknown avg `-0.0573` n `764`
- 1h: commodity avg `0.0998` n `12`; crypto_alt avg `-0.2526` n `228`; crypto_major avg `-0.195` n `8`; equity avg `-0.2881` n `86`; fx avg `0.0093` n `6`; index avg `-0.0846` n `23`; metal avg `-0.0172` n `20`; unknown avg `-0.1136` n `764`
- 4h: commodity avg `0.0788` n `12`; crypto_alt avg `-1.0834` n `228`; crypto_major avg `-1.6151` n `8`; equity avg `-0.4065` n `86`; fx avg `-0.1006` n `6`; index avg `-0.0766` n `23`; metal avg `0.0359` n `20`; unknown avg `-0.4206` n `620`
- 24h: commodity avg `-0.5961` n `12`; crypto_alt avg `-4.1361` n `228`; crypto_major avg `-4.2535` n `8`; equity avg `-4.5609` n `85`; fx avg `-0.1433` n `6`; index avg `-0.9051` n `23`; metal avg `-1.2706` n `20`; unknown avg `0.297` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
