# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T23:37:42.776974+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `12`; crypto_alt avg `0.0619` n `230`; crypto_major avg `0.0596` n `8`; equity avg `-0.1131` n `120`; fx avg `-0.0036` n `6`; index avg `-0.0178` n `25`; metal avg `-0.0559` n `20`; unknown avg `-0.106` n `789`
- 1h: commodity avg `0.0085` n `12`; crypto_alt avg `0.1053` n `230`; crypto_major avg `0.1421` n `8`; equity avg `-0.2373` n `120`; fx avg `-0.0055` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0669` n `20`; unknown avg `-0.192` n `789`
- 4h: commodity avg `0.1083` n `12`; crypto_alt avg `-0.1742` n `230`; crypto_major avg `-0.0736` n `8`; equity avg `-0.5915` n `120`; fx avg `-0.0139` n `6`; index avg `-0.0579` n `25`; metal avg `-0.2203` n `20`; unknown avg `0.0866` n `789`
- 24h: commodity avg `0.3071` n `12`; crypto_alt avg `-0.4273` n `230`; crypto_major avg `0.0634` n `8`; equity avg `-4.8121` n `120`; fx avg `-0.0368` n `6`; index avg `-0.7177` n `25`; metal avg `-0.9133` n `20`; unknown avg `-0.2276` n `755`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
