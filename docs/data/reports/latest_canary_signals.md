# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T00:37:29.349576+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0297` n `13`; crypto_alt avg `-0.0277` n `239`; crypto_major avg `-0.1284` n `8`; equity avg `-0.1341` n `160`; fx avg `-0.0102` n `6`; index avg `-0.0227` n `27`; metal avg `-0.0372` n `20`; unknown avg `0.2689` n `1261`
- 1h: commodity avg `0.0503` n `13`; crypto_alt avg `-0.056` n `239`; crypto_major avg `-0.2179` n `8`; equity avg `0.0382` n `160`; fx avg `0.0357` n `6`; index avg `-0.0504` n `27`; metal avg `-0.0955` n `20`; unknown avg `0.2003` n `1249`
- 4h: commodity avg `-0.0166` n `13`; crypto_alt avg `-0.7642` n `239`; crypto_major avg `-0.0729` n `8`; equity avg `-0.1655` n `160`; fx avg `0.0777` n `6`; index avg `-0.0849` n `27`; metal avg `-0.1562` n `20`; unknown avg `-0.2324` n `1209`
- 24h: commodity avg `-0.3517` n `13`; crypto_alt avg `1.1696` n `239`; crypto_major avg `-0.2882` n `8`; equity avg `5.2921` n `160`; fx avg `-0.0158` n `6`; index avg `0.5987` n `27`; metal avg `0.2937` n `20`; unknown avg `5.0011` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
