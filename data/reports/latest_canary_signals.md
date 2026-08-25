# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T07:56:10.882703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0651` n `12`; crypto_alt avg `-1.0294` n `231`; crypto_major avg `-0.8147` n `8`; equity avg `-0.0716` n `122`; fx avg `-0.0058` n `6`; index avg `-0.0082` n `25`; metal avg `-0.0334` n `20`; unknown avg `-0.1339` n `794`
- 1h: commodity avg `0.0613` n `12`; crypto_alt avg `-0.736` n `231`; crypto_major avg `-0.5564` n `8`; equity avg `-0.1163` n `122`; fx avg `0.0213` n `6`; index avg `-0.035` n `25`; metal avg `-0.0811` n `20`; unknown avg `-0.105` n `794`
- 4h: commodity avg `-0.1743` n `12`; crypto_alt avg `-1.033` n `231`; crypto_major avg `-0.8025` n `8`; equity avg `0.5564` n `122`; fx avg `0.0305` n `6`; index avg `0.1115` n `25`; metal avg `-0.0156` n `20`; unknown avg `-0.185` n `778`
- 24h: commodity avg `-0.2084` n `12`; crypto_alt avg `0.6503` n `231`; crypto_major avg `1.6572` n `8`; equity avg `0.2204` n `122`; fx avg `0.0367` n `6`; index avg `0.036` n `25`; metal avg `-0.174` n `20`; unknown avg `0.4326` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
