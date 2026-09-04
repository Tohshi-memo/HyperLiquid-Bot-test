# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T14:07:25.308282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.86` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-2.3058` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.9022` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6341` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0379` n `12`; crypto_alt avg `-0.2459` n `232`; crypto_major avg `-0.1859` n `8`; equity avg `0.3196` n `133`; fx avg `0.0269` n `6`; index avg `0.0088` n `26`; metal avg `-0.0603` n `20`; unknown avg `0.6755` n `791`
- 1h: commodity avg `-0.1831` n `12`; crypto_alt avg `0.6033` n `232`; crypto_major avg `0.2075` n `8`; equity avg `1.378` n `133`; fx avg `0.0005` n `6`; index avg `0.1802` n `26`; metal avg `0.1516` n `20`; unknown avg `1.0444` n `761`
- 4h: commodity avg `-0.2634` n `12`; crypto_alt avg `-1.4058` n `232`; crypto_major avg `-1.8427` n `8`; equity avg `0.4631` n `133`; fx avg `-0.1288` n `6`; index avg `0.0595` n `26`; metal avg `-0.2086` n `20`; unknown avg `-0.1831` n `741`
- 24h: commodity avg `-0.6034` n `12`; crypto_alt avg `1.0228` n `232`; crypto_major avg `1.0881` n `8`; equity avg `2.7966` n `133`; fx avg `-0.0794` n `6`; index avg `0.4065` n `26`; metal avg `-0.0327` n `20`; unknown avg `1.1069` n `702`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
