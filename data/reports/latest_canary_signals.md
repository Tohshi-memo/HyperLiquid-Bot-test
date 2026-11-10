# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T07:37:24.677984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0904` n `13`; crypto_alt avg `0.0585` n `239`; crypto_major avg `0.1097` n `8`; equity avg `0.0627` n `160`; fx avg `-0.0136` n `6`; index avg `0.0053` n `27`; metal avg `-0.0217` n `20`; unknown avg `-0.0175` n `1261`
- 1h: commodity avg `-0.137` n `13`; crypto_alt avg `0.1305` n `239`; crypto_major avg `0.2934` n `8`; equity avg `-0.0237` n `160`; fx avg `-0.0084` n `6`; index avg `-0.008` n `27`; metal avg `-0.1391` n `20`; unknown avg `0.862` n `1255`
- 4h: commodity avg `-0.1142` n `13`; crypto_alt avg `0.7567` n `239`; crypto_major avg `0.6388` n `8`; equity avg `0.2895` n `160`; fx avg `-0.0885` n `6`; index avg `0.0736` n `27`; metal avg `-0.1101` n `20`; unknown avg `1.7657` n `1217`
- 24h: commodity avg `-0.4606` n `13`; crypto_alt avg `2.6903` n `239`; crypto_major avg `1.2944` n `8`; equity avg `5.2481` n `160`; fx avg `0.0156` n `6`; index avg `0.6018` n `27`; metal avg `0.2446` n `20`; unknown avg `191.5965` n `1071`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
