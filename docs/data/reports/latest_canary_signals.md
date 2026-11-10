# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T05:07:33.392946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `13`; crypto_alt avg `0.1746` n `239`; crypto_major avg `0.2712` n `8`; equity avg `-0.0113` n `160`; fx avg `0.0053` n `6`; index avg `0.0006` n `27`; metal avg `-0.013` n `20`; unknown avg `-0.0608` n `1255`
- 1h: commodity avg `-0.0392` n `13`; crypto_alt avg `0.2685` n `239`; crypto_major avg `0.3681` n `8`; equity avg `0.3434` n `160`; fx avg `0.001` n `6`; index avg `0.0362` n `27`; metal avg `0.0415` n `20`; unknown avg `0.1606` n `1249`
- 4h: commodity avg `-0.2185` n `13`; crypto_alt avg `0.2092` n `239`; crypto_major avg `-0.2999` n `8`; equity avg `-0.1037` n `160`; fx avg `-0.0007` n `6`; index avg `-0.0157` n `27`; metal avg `-0.1263` n `20`; unknown avg `-0.1117` n `1235`
- 24h: commodity avg `-0.7392` n `13`; crypto_alt avg `1.3877` n `239`; crypto_major avg `0.0269` n `8`; equity avg `3.7732` n `160`; fx avg `0.0399` n `6`; index avg `0.3536` n `27`; metal avg `0.0606` n `20`; unknown avg `188.8826` n `1069`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
