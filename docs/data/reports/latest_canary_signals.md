# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T10:07:29.241598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0704` n `12`; crypto_alt avg `0.091` n `230`; crypto_major avg `0.1745` n `8`; equity avg `0.0991` n `98`; fx avg `-0.0087` n `6`; index avg `0.0374` n `25`; metal avg `0.009` n `20`; unknown avg `0.0279` n `773`
- 1h: commodity avg `0.1074` n `12`; crypto_alt avg `0.055` n `230`; crypto_major avg `0.0224` n `8`; equity avg `-0.0571` n `98`; fx avg `0.0153` n `6`; index avg `-0.0068` n `25`; metal avg `-0.0124` n `20`; unknown avg `-0.0224` n `773`
- 4h: commodity avg `0.4125` n `12`; crypto_alt avg `0.2467` n `230`; crypto_major avg `0.1859` n `8`; equity avg `0.0429` n `98`; fx avg `-0.0225` n `6`; index avg `-0.0221` n `25`; metal avg `-0.1053` n `20`; unknown avg `0.0757` n `772`
- 24h: commodity avg `0.7353` n `12`; crypto_alt avg `-0.784` n `230`; crypto_major avg `-1.5332` n `8`; equity avg `0.4751` n `98`; fx avg `-0.0047` n `6`; index avg `-0.0015` n `25`; metal avg `0.3524` n `20`; unknown avg `0.0992` n `739`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1037`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0785`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0686`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0679`, n `666`, weak_sample_signal
