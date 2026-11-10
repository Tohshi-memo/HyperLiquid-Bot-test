# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T06:37:30.369748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0516` n `13`; crypto_alt avg `0.0649` n `239`; crypto_major avg `-0.0319` n `8`; equity avg `-0.1609` n `160`; fx avg `-0.0037` n `6`; index avg `-0.0171` n `27`; metal avg `-0.0131` n `20`; unknown avg `0.6272` n `1257`
- 1h: commodity avg `-0.1495` n `13`; crypto_alt avg `-0.0093` n `239`; crypto_major avg `-0.3281` n `8`; equity avg `-0.3071` n `160`; fx avg `0.0018` n `6`; index avg `-0.029` n `27`; metal avg `-0.043` n `20`; unknown avg `1.1462` n `1233`
- 4h: commodity avg `-0.0939` n `13`; crypto_alt avg `0.6141` n `239`; crypto_major avg `0.1509` n `8`; equity avg `-0.1801` n `160`; fx avg `-0.1047` n `6`; index avg `0.0209` n `27`; metal avg `0.0234` n `20`; unknown avg `1.7369` n `1213`
- 24h: commodity avg `-0.4611` n `13`; crypto_alt avg `1.9225` n `239`; crypto_major avg `0.5364` n `8`; equity avg `4.4924` n `160`; fx avg `0.0317` n `6`; index avg `0.5134` n `27`; metal avg `0.243` n `20`; unknown avg `192.4161` n `1063`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
