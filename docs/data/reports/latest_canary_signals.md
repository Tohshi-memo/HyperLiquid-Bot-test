# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T15:52:27.829230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0501` n `13`; crypto_alt avg `-0.2078` n `239`; crypto_major avg `-0.2698` n `8`; equity avg `0.3274` n `161`; fx avg `0.0054` n `6`; index avg `0.0528` n `27`; metal avg `-0.0426` n `20`; unknown avg `0.6791` n `1259`
- 1h: commodity avg `0.2322` n `13`; crypto_alt avg `0.6121` n `239`; crypto_major avg `0.7602` n `8`; equity avg `1.6135` n `161`; fx avg `0.0403` n `6`; index avg `0.1519` n `27`; metal avg `-0.0651` n `20`; unknown avg `0.2431` n `1253`
- 4h: commodity avg `0.4987` n `13`; crypto_alt avg `0.6529` n `239`; crypto_major avg `0.6322` n `8`; equity avg `1.3079` n `161`; fx avg `0.0094` n `6`; index avg `0.104` n `27`; metal avg `-0.2734` n `20`; unknown avg `18.9905` n `1229`
- 24h: commodity avg `1.2789` n `13`; crypto_alt avg `1.2988` n `239`; crypto_major avg `1.8927` n `8`; equity avg `5.2914` n `161`; fx avg `-0.1251` n `6`; index avg `0.4844` n `27`; metal avg `0.1857` n `20`; unknown avg `2.9082` n `1153`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.339`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
