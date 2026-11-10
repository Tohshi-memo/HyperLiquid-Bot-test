# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T18:52:28.198515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `13`; crypto_alt avg `-0.17` n `239`; crypto_major avg `-0.1084` n `8`; equity avg `-0.0195` n `160`; fx avg `0.0151` n `6`; index avg `0.0018` n `27`; metal avg `-0.0068` n `20`; unknown avg `19.0878` n `1264`
- 1h: commodity avg `-0.0382` n `13`; crypto_alt avg `0.4897` n `239`; crypto_major avg `0.5872` n `8`; equity avg `0.2297` n `160`; fx avg `0.0252` n `6`; index avg `0.0316` n `27`; metal avg `0.0566` n `20`; unknown avg `-0.2793` n `1256`
- 4h: commodity avg `0.3898` n `13`; crypto_alt avg `-1.4062` n `239`; crypto_major avg `-1.1136` n `8`; equity avg `-1.1703` n `160`; fx avg `-0.0599` n `6`; index avg `-0.1222` n `27`; metal avg `-0.0393` n `20`; unknown avg `-1.0042` n `1250`
- 24h: commodity avg `-0.3177` n `13`; crypto_alt avg `-1.4781` n `239`; crypto_major avg `-2.6592` n `8`; equity avg `-1.9481` n `160`; fx avg `-0.0924` n `6`; index avg `-0.2095` n `27`; metal avg `-0.4762` n `20`; unknown avg `0.3213` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2457`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
