# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T15:07:39.360618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0731` n `13`; crypto_alt avg `0.7054` n `239`; crypto_major avg `0.7088` n `8`; equity avg `1.2138` n `160`; fx avg `-0.018` n `6`; index avg `0.1249` n `27`; metal avg `0.1508` n `20`; unknown avg `1.5548` n `1258`
- 1h: commodity avg `0.2642` n `13`; crypto_alt avg `1.1705` n `239`; crypto_major avg `0.5693` n `8`; equity avg `2.0678` n `160`; fx avg `-0.0174` n `6`; index avg `0.184` n `27`; metal avg `-0.0046` n `20`; unknown avg `22.3456` n `1256`
- 4h: commodity avg `-0.0449` n `13`; crypto_alt avg `1.4039` n `239`; crypto_major avg `0.0719` n `8`; equity avg `0.8744` n `160`; fx avg `-0.0279` n `6`; index avg `0.0841` n `27`; metal avg `-0.1129` n `20`; unknown avg `2.2111` n `1250`
- 24h: commodity avg `-0.4411` n `13`; crypto_alt avg `0.4174` n `239`; crypto_major avg `-1.1879` n `8`; equity avg `1.5905` n `160`; fx avg `-0.0588` n `6`; index avg `0.1613` n `27`; metal avg `-0.2425` n `20`; unknown avg `1.8084` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2228`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
