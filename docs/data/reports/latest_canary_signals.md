# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T19:52:29.412993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0577` n `12`; crypto_alt avg `0.0317` n `230`; crypto_major avg `0.0097` n `8`; equity avg `-0.015` n `96`; fx avg `-0.0013` n `6`; index avg `-0.0064` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.0187` n `770`
- 1h: commodity avg `-0.1331` n `12`; crypto_alt avg `0.077` n `230`; crypto_major avg `0.0499` n `8`; equity avg `-0.011` n `96`; fx avg `0.0045` n `6`; index avg `0.003` n `25`; metal avg `0.0041` n `20`; unknown avg `-0.0212` n `770`
- 4h: commodity avg `0.1845` n `12`; crypto_alt avg `0.2151` n `230`; crypto_major avg `0.4575` n `8`; equity avg `-0.0348` n `96`; fx avg `-0.0685` n `6`; index avg `-0.0382` n `25`; metal avg `-0.0188` n `20`; unknown avg `0.0258` n `770`
- 24h: commodity avg `0.4485` n `12`; crypto_alt avg `-0.5824` n `230`; crypto_major avg `0.125` n `8`; equity avg `-0.64` n `96`; fx avg `-0.1451` n `6`; index avg `-0.0513` n `25`; metal avg `-0.0225` n `20`; unknown avg `-0.0428` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
