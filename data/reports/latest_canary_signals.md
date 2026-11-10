# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T04:07:28.376734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0675` n `13`; crypto_alt avg `0.3184` n `239`; crypto_major avg `0.153` n `8`; equity avg `0.03` n `160`; fx avg `0.0082` n `6`; index avg `0.0009` n `27`; metal avg `0.0061` n `20`; unknown avg `0.1253` n `1249`
- 1h: commodity avg `0.0035` n `13`; crypto_alt avg `0.1844` n `239`; crypto_major avg `-0.1821` n `8`; equity avg `-0.5705` n `160`; fx avg `-0.0216` n `6`; index avg `-0.0526` n `27`; metal avg `-0.0453` n `20`; unknown avg `0.1835` n `1241`
- 4h: commodity avg `-0.1318` n `13`; crypto_alt avg `-0.2145` n `239`; crypto_major avg `-0.7863` n `8`; equity avg `-1.0719` n `160`; fx avg `-0.0058` n `6`; index avg `-0.1402` n `27`; metal avg `-0.1068` n `20`; unknown avg `0.6373` n `1239`
- 24h: commodity avg `-0.7808` n `13`; crypto_alt avg `0.6719` n `239`; crypto_major avg `-0.77` n `8`; equity avg `2.9562` n `160`; fx avg `0.0189` n `6`; index avg `0.2815` n `27`; metal avg `0.027` n `20`; unknown avg `188.0594` n `1067`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
