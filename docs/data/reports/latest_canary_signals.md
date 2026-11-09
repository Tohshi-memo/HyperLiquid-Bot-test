# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T12:07:29.555261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0907` n `13`; crypto_alt avg `0.4452` n `239`; crypto_major avg `0.2674` n `8`; equity avg `0.1387` n `158`; fx avg `-0.004` n `6`; index avg `-0.0059` n `27`; metal avg `-0.0384` n `20`; unknown avg `18.9902` n `1253`
- 1h: commodity avg `-0.2497` n `13`; crypto_alt avg `0.8462` n `239`; crypto_major avg `0.5495` n `8`; equity avg `0.3162` n `158`; fx avg `-0.0443` n `6`; index avg `0.019` n `27`; metal avg `0.0357` n `20`; unknown avg `19.8632` n `1251`
- 4h: commodity avg `-0.2818` n `13`; crypto_alt avg `2.4045` n `239`; crypto_major avg `0.9119` n `8`; equity avg `1.3649` n `158`; fx avg `-0.0001` n `6`; index avg `0.1643` n `27`; metal avg `0.1187` n `20`; unknown avg `160.3677` n `1205`
- 24h: commodity avg `-0.5225` n `13`; crypto_alt avg `-1.2689` n `239`; crypto_major avg `-3.5346` n `8`; equity avg `-0.1655` n `158`; fx avg `-0.1509` n `6`; index avg `-0.0047` n `27`; metal avg `0.2946` n `20`; unknown avg `0.3436` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
