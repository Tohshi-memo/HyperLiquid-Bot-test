# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T05:07:19.283857+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0478` n `12`; crypto_alt avg `-0.0227` n `228`; crypto_major avg `0.0549` n `8`; equity avg `-0.0165` n `69`; fx avg `-0.0064` n `6`; index avg `0.0099` n `23`; metal avg `0.0143` n `18`; unknown avg `0.7118` n `421`
- 1h: commodity avg `0.1343` n `12`; crypto_alt avg `0.2349` n `228`; crypto_major avg `0.2082` n `8`; equity avg `-0.0028` n `69`; fx avg `-0.0026` n `6`; index avg `-0.0069` n `23`; metal avg `-0.0127` n `18`; unknown avg `-0.1848` n `421`
- 4h: commodity avg `0.111` n `12`; crypto_alt avg `0.5434` n `228`; crypto_major avg `0.4276` n `8`; equity avg `0.1261` n `69`; fx avg `0.0178` n `6`; index avg `-0.0266` n `23`; metal avg `-0.0407` n `18`; unknown avg `0.5649` n `419`
- 24h: commodity avg `0.1149` n `12`; crypto_alt avg `0.8362` n `228`; crypto_major avg `2.6843` n `8`; equity avg `0.9408` n `69`; fx avg `0.047` n `6`; index avg `0.0648` n `23`; metal avg `-0.044` n `18`; unknown avg `0.7147` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
