# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T16:37:22.973707+00:00`
- Correlation status: `ready`
- Asset price records: `470`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `6.93` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.1443` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.7647` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5911` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1222` n `12`; crypto_alt avg `-0.1275` n `228`; crypto_major avg `-0.0414` n `8`; equity avg `0.0013` n `65`; fx avg `0.0036` n `4`; index avg `0.0153` n `23`; metal avg `0.0305` n `18`; unknown avg `-0.0735` n `356`
- 1h: commodity avg `-0.0914` n `12`; crypto_alt avg `0.238` n `228`; crypto_major avg `0.0199` n `8`; equity avg `0.1903` n `65`; fx avg `0.0301` n `4`; index avg `0.0236` n `23`; metal avg `-0.0637` n `18`; unknown avg `0.0234` n `356`
- 4h: commodity avg `-0.3255` n `7`; crypto_alt avg `-0.9734` n `223`; crypto_major avg `-1.808` n `7`; equity avg `-0.0433` n `47`; fx avg `0.0448` n `4`; index avg `-0.2169` n `6`; metal avg `0.3363` n `7`; unknown avg `7.7514` n `313`
- 24h: commodity avg `-2.6478` n `7`; crypto_alt avg `2.7663` n `223`; crypto_major avg `0.9013` n `7`; equity avg `2.3862` n `47`; fx avg `-0.4307` n `4`; index avg `1.7912` n `6`; metal avg `3.1984` n `7`; unknown avg `16.2759` n `311`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2122`, n `466`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1633`, n `462`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.147`, n `462`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1354`, n `466`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1231`, n `466`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1219`, n `466`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `466`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1198`, n `462`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1059`, n `466`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.105`, n `462`, weak_sample_signal
