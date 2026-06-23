# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T07:07:27.146987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2716` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.057` n `12`; crypto_alt avg `0.1825` n `228`; crypto_major avg `0.118` n `8`; equity avg `0.1545` n `86`; fx avg `-0.0392` n `6`; index avg `0.031` n `23`; metal avg `0.0281` n `20`; unknown avg `0.0338` n `716`
- 1h: commodity avg `-0.0345` n `12`; crypto_alt avg `-0.8836` n `228`; crypto_major avg `-0.4366` n `8`; equity avg `0.2512` n `86`; fx avg `-0.0088` n `6`; index avg `-0.0475` n `23`; metal avg `-0.0182` n `20`; unknown avg `-0.3273` n `716`
- 4h: commodity avg `-0.1501` n `12`; crypto_alt avg `-1.6406` n `228`; crypto_major avg `-1.6806` n `8`; equity avg `-1.3995` n `86`; fx avg `-0.0127` n `6`; index avg `-0.409` n `23`; metal avg `-0.3369` n `20`; unknown avg `-0.0487` n `676`
- 24h: commodity avg `-0.6928` n `12`; crypto_alt avg `-2.6395` n `228`; crypto_major avg `-2.2704` n `8`; equity avg `-3.929` n `85`; fx avg `-0.0396` n `6`; index avg `-0.7576` n `23`; metal avg `-1.4576` n `18`; unknown avg `0.5644` n `647`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
