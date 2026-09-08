# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T04:22:31.628892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `-0.0601` n `232`; crypto_major avg `-0.0482` n `8`; equity avg `-0.0684` n `134`; fx avg `0.0211` n `6`; index avg `-0.0109` n `26`; metal avg `-0.03` n `20`; unknown avg `1.0879` n `797`
- 1h: commodity avg `0.0374` n `12`; crypto_alt avg `0.1315` n `232`; crypto_major avg `0.1525` n `8`; equity avg `0.146` n `134`; fx avg `0.0373` n `6`; index avg `0.0112` n `26`; metal avg `0.0312` n `20`; unknown avg `0.9406` n `795`
- 4h: commodity avg `0.024` n `12`; crypto_alt avg `-0.0534` n `232`; crypto_major avg `-0.338` n `8`; equity avg `0.3929` n `134`; fx avg `-0.0335` n `6`; index avg `0.0997` n `26`; metal avg `0.0862` n `20`; unknown avg `121.7743` n `783`
- 24h: commodity avg `0.1233` n `12`; crypto_alt avg `0.4009` n `232`; crypto_major avg `-1.0344` n `8`; equity avg `0.7018` n `134`; fx avg `-0.3009` n `6`; index avg `0.2034` n `26`; metal avg `0.4064` n `20`; unknown avg `7375.8737` n `678`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
