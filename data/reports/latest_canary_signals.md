# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T22:52:24.606749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0247` n `12`; crypto_alt avg `-0.0212` n `229`; crypto_major avg `0.009` n `8`; equity avg `-0.0102` n `88`; fx avg `-0.0055` n `6`; index avg `-0.0122` n `25`; metal avg `0.0199` n `20`; unknown avg `0.0595` n `765`
- 1h: commodity avg `-0.1631` n `12`; crypto_alt avg `0.1225` n `229`; crypto_major avg `0.5586` n `8`; equity avg `0.1217` n `88`; fx avg `0.0447` n `6`; index avg `-0.0065` n `25`; metal avg `0.1685` n `20`; unknown avg `0.5178` n `765`
- 4h: commodity avg `-0.1486` n `12`; crypto_alt avg `0.5384` n `229`; crypto_major avg `0.8614` n `8`; equity avg `0.1534` n `88`; fx avg `0.0851` n `6`; index avg `-0.0224` n `25`; metal avg `0.1509` n `20`; unknown avg `1.5448` n `765`
- 24h: commodity avg `-0.1768` n `12`; crypto_alt avg `-0.0711` n `229`; crypto_major avg `0.6455` n `8`; equity avg `0.4167` n `88`; fx avg `0.0238` n `6`; index avg `0.0505` n `25`; metal avg `0.1705` n `20`; unknown avg `1.1776` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
