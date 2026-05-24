# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T12:10:34.428637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0378` n `12`; crypto_alt avg `-0.158` n `228`; crypto_major avg `-0.1311` n `8`; equity avg `-0.0297` n `67`; fx avg `0.0024` n `6`; index avg `0.015` n `23`; metal avg `-0.035` n `18`; unknown avg `0.1993` n `396`
- 1h: commodity avg `-0.0272` n `12`; crypto_alt avg `-0.2672` n `228`; crypto_major avg `-0.12` n `8`; equity avg `-0.0416` n `67`; fx avg `-0.0133` n `6`; index avg `-0.0231` n `23`; metal avg `-0.0187` n `18`; unknown avg `0.3458` n `396`
- 4h: commodity avg `0.1304` n `12`; crypto_alt avg `0.0714` n `228`; crypto_major avg `0.579` n `8`; equity avg `0.2115` n `67`; fx avg `-0.0104` n `6`; index avg `-0.0004` n `23`; metal avg `-0.0505` n `18`; unknown avg `0.2269` n `396`
- 24h: commodity avg `-2.6072` n `12`; crypto_alt avg `3.8945` n `228`; crypto_major avg `4.7072` n `8`; equity avg `2.7502` n `67`; fx avg `0.0519` n `6`; index avg `1.2938` n `23`; metal avg `1.2895` n `18`; unknown avg `1.5773` n `386`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
