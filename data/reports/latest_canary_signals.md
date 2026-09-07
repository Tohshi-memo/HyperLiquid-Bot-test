# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T09:43:59.772082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `12`; crypto_alt avg `-0.1999` n `232`; crypto_major avg `-0.1648` n `8`; equity avg `-0.0122` n `134`; fx avg `-0.0083` n `6`; index avg `-0.0023` n `26`; metal avg `0.009` n `20`; unknown avg `0.5222` n `796`
- 1h: commodity avg `0.0932` n `12`; crypto_alt avg `0.3719` n `232`; crypto_major avg `0.1553` n `8`; equity avg `-0.0166` n `134`; fx avg `0.0043` n `6`; index avg `-0.0097` n `26`; metal avg `-0.0687` n `20`; unknown avg `0.5867` n `790`
- 4h: commodity avg `-0.1536` n `12`; crypto_alt avg `-0.148` n `232`; crypto_major avg `-0.4788` n `8`; equity avg `0.0245` n `134`; fx avg `-0.1267` n `6`; index avg `0.0285` n `26`; metal avg `0.0619` n `20`; unknown avg `1.8886` n `758`
- 24h: commodity avg `-0.0684` n `12`; crypto_alt avg `0.3288` n `232`; crypto_major avg `-0.9273` n `8`; equity avg `0.3627` n `134`; fx avg `-0.1294` n `6`; index avg `0.0377` n `26`; metal avg `-0.0784` n `20`; unknown avg `76.0515` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
