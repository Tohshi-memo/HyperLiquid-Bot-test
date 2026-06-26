# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T12:24:42.494948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5727` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.2829` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `0.2241` n `228`; crypto_major avg `0.28` n `8`; equity avg `-0.0974` n `86`; fx avg `0.0003` n `6`; index avg `-0.0066` n `23`; metal avg `-0.0106` n `20`; unknown avg `0.005` n `765`
- 1h: commodity avg `0.0292` n `12`; crypto_alt avg `0.2439` n `228`; crypto_major avg `0.1785` n `8`; equity avg `-0.0891` n `86`; fx avg `-0.0168` n `6`; index avg `-0.0161` n `23`; metal avg `-0.0725` n `20`; unknown avg `0.0259` n `765`
- 4h: commodity avg `0.0167` n `12`; crypto_alt avg `-0.9759` n `228`; crypto_major avg `-1.352` n `8`; equity avg `-0.4671` n `86`; fx avg `0.0063` n `6`; index avg `-0.0691` n `23`; metal avg `0.2207` n `20`; unknown avg `-0.15` n `765`
- 24h: commodity avg `0.0517` n `12`; crypto_alt avg `-1.4974` n `228`; crypto_major avg `-1.5768` n `8`; equity avg `-4.1281` n `86`; fx avg `0.0678` n `6`; index avg `-0.6026` n `23`; metal avg `0.5914` n `20`; unknown avg `0.7414` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2831`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1945`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
