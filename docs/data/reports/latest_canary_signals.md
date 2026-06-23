# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T07:22:30.177223+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2483` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0591` n `12`; crypto_alt avg `0.1358` n `228`; crypto_major avg `0.056` n `8`; equity avg `0.1738` n `86`; fx avg `0.0044` n `6`; index avg `0.012` n `23`; metal avg `0.0662` n `20`; unknown avg `-0.1015` n `716`
- 1h: commodity avg `-0.0993` n `12`; crypto_alt avg `0.9189` n `228`; crypto_major avg `0.6885` n `8`; equity avg `0.7393` n `86`; fx avg `-0.0404` n `6`; index avg `0.0496` n `23`; metal avg `0.0154` n `20`; unknown avg `-0.056` n `716`
- 4h: commodity avg `-0.1942` n `12`; crypto_alt avg `-1.5002` n `228`; crypto_major avg `-1.6099` n `8`; equity avg `-0.9083` n `86`; fx avg `0.0017` n `6`; index avg `-0.3616` n `23`; metal avg `-0.1537` n `20`; unknown avg `-0.039` n `676`
- 24h: commodity avg `-0.7503` n `12`; crypto_alt avg `-2.8069` n `228`; crypto_major avg `-2.57` n `8`; equity avg `-3.8527` n `85`; fx avg `-0.0499` n `6`; index avg `-0.7533` n `23`; metal avg `-1.401` n `18`; unknown avg `0.4949` n `647`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
