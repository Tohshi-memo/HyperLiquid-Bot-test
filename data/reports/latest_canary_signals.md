# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T23:22:30.325622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.025` n `12`; crypto_alt avg `0.1933` n `232`; crypto_major avg `0.13` n `8`; equity avg `0.0098` n `134`; fx avg `-0.0091` n `6`; index avg `-0.0111` n `26`; metal avg `-0.0179` n `20`; unknown avg `-0.055` n `794`
- 1h: commodity avg `-0.026` n `12`; crypto_alt avg `0.6655` n `232`; crypto_major avg `0.7611` n `8`; equity avg `0.0022` n `134`; fx avg `-0.0185` n `6`; index avg `-0.0308` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.0584` n `791`
- 4h: commodity avg `-0.0248` n `12`; crypto_alt avg `0.8587` n `232`; crypto_major avg `0.7374` n `8`; equity avg `-0.0415` n `134`; fx avg `0.019` n `6`; index avg `-0.029` n `26`; metal avg `-0.0675` n `20`; unknown avg `-0.1346` n `771`
- 24h: commodity avg `0.0094` n `12`; crypto_alt avg `1.54` n `232`; crypto_major avg `1.0312` n `8`; equity avg `0.2433` n `134`; fx avg `0.0203` n `6`; index avg `-0.0186` n `26`; metal avg `-0.0886` n `20`; unknown avg `151.6694` n `678`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
