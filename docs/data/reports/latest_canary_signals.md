# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T13:22:15.384248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0821` n `12`; crypto_alt avg `0.0134` n `228`; crypto_major avg `-0.0228` n `8`; equity avg `-0.0272` n `67`; fx avg `-0.001` n `6`; index avg `0.009` n `23`; metal avg `0.0327` n `18`; unknown avg `0.0691` n `396`
- 1h: commodity avg `0.1189` n `12`; crypto_alt avg `0.2458` n `228`; crypto_major avg `0.3494` n `8`; equity avg `0.1024` n `67`; fx avg `0.0209` n `6`; index avg `-0.0621` n `23`; metal avg `-0.0584` n `18`; unknown avg `0.3806` n `396`
- 4h: commodity avg `0.2165` n `12`; crypto_alt avg `-0.4644` n `228`; crypto_major avg `0.1362` n `8`; equity avg `0.2403` n `67`; fx avg `0.0041` n `6`; index avg `-0.0845` n `23`; metal avg `-0.1156` n `18`; unknown avg `0.1311` n `396`
- 24h: commodity avg `-2.6097` n `12`; crypto_alt avg `2.5521` n `228`; crypto_major avg `4.1711` n `8`; equity avg `2.6009` n `67`; fx avg `0.0714` n `6`; index avg `1.0828` n `23`; metal avg `1.1578` n `18`; unknown avg `1.9186` n `386`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
