# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T17:52:32.135027+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5365` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0772` n `12`; crypto_alt avg `0.1964` n `228`; crypto_major avg `0.3051` n `8`; equity avg `0.1762` n `85`; fx avg `-0.0052` n `6`; index avg `0.006` n `23`; metal avg `0.0424` n `20`; unknown avg `0.0818` n `717`
- 1h: commodity avg `-0.1354` n `12`; crypto_alt avg `-0.1266` n `228`; crypto_major avg `0.1053` n `8`; equity avg `0.1271` n `85`; fx avg `-0.0156` n `6`; index avg `0.0033` n `23`; metal avg `-0.0848` n `20`; unknown avg `-0.0271` n `717`
- 4h: commodity avg `-0.0797` n `12`; crypto_alt avg `-1.4904` n `228`; crypto_major avg `-1.5988` n `8`; equity avg `-1.1976` n `85`; fx avg `-0.0552` n `6`; index avg `-0.0623` n `23`; metal avg `-0.4347` n `20`; unknown avg `0.5683` n `716`
- 24h: commodity avg `-0.9336` n `12`; crypto_alt avg `-0.4016` n `228`; crypto_major avg `-0.0519` n `8`; equity avg `-0.491` n `85`; fx avg `0.0403` n `6`; index avg `0.1417` n `23`; metal avg `0.109` n `18`; unknown avg `1.0786` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
