# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T23:07:23.783780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `12`; crypto_alt avg `0.0906` n `232`; crypto_major avg `0.1608` n `8`; equity avg `-0.031` n `134`; fx avg `0.0003` n `6`; index avg `-0.0201` n `26`; metal avg `-0.0086` n `20`; unknown avg `-0.182` n `792`
- 1h: commodity avg `-0.042` n `12`; crypto_alt avg `0.1903` n `232`; crypto_major avg `0.3735` n `8`; equity avg `-0.0484` n `134`; fx avg `0.0083` n `6`; index avg `-0.0275` n `26`; metal avg `0.036` n `20`; unknown avg `0.48` n `791`
- 4h: commodity avg `-0.0562` n `12`; crypto_alt avg `0.5601` n `232`; crypto_major avg `0.4966` n `8`; equity avg `-0.0387` n `134`; fx avg `0.0255` n `6`; index avg `-0.0181` n `26`; metal avg `-0.0445` n `20`; unknown avg `0.0608` n `771`
- 24h: commodity avg `-0.0328` n `12`; crypto_alt avg `1.3203` n `232`; crypto_major avg `0.8609` n `8`; equity avg `0.2419` n `134`; fx avg `0.029` n `6`; index avg `-0.0129` n `26`; metal avg `-0.0714` n `20`; unknown avg `151.6667` n `678`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
