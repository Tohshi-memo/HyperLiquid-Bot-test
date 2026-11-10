# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T09:22:24.933508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `13`; crypto_alt avg `0.2467` n `239`; crypto_major avg `0.0947` n `8`; equity avg `0.1324` n `160`; fx avg `-0.0085` n `6`; index avg `0.009` n `27`; metal avg `-0.0091` n `20`; unknown avg `-0.0674` n `1260`
- 1h: commodity avg `-0.0677` n `13`; crypto_alt avg `0.0695` n `239`; crypto_major avg `-0.3298` n `8`; equity avg `-0.0529` n `160`; fx avg `0.0047` n `6`; index avg `-0.0198` n `27`; metal avg `-0.1055` n `20`; unknown avg `2.1676` n `1235`
- 4h: commodity avg `-0.2757` n `13`; crypto_alt avg `0.1543` n `239`; crypto_major avg `-0.6239` n `8`; equity avg `0.0369` n `160`; fx avg `-0.0324` n `6`; index avg `-0.005` n `27`; metal avg `-0.2545` n `20`; unknown avg `4.2523` n `1199`
- 24h: commodity avg `-0.806` n `13`; crypto_alt avg `1.5402` n `239`; crypto_major avg `0.0539` n `8`; equity avg `4.7168` n `160`; fx avg `-0.045` n `6`; index avg `0.5236` n `27`; metal avg `0.1063` n `20`; unknown avg `5.6991` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
