# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T05:52:28.080277+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0376` n `13`; crypto_alt avg `0.2615` n `239`; crypto_major avg `0.182` n `8`; equity avg `0.067` n `160`; fx avg `0.0019` n `6`; index avg `0.0137` n `27`; metal avg `0.0104` n `20`; unknown avg `0.9383` n `1259`
- 1h: commodity avg `0.1269` n `13`; crypto_alt avg `0.4851` n `239`; crypto_major avg `0.6319` n `8`; equity avg `0.4772` n `160`; fx avg `-0.0659` n `6`; index avg `0.1011` n `27`; metal avg `0.062` n `20`; unknown avg `0.8348` n `1249`
- 4h: commodity avg `0.0342` n `13`; crypto_alt avg `0.6248` n `239`; crypto_major avg `0.1658` n `8`; equity avg `0.2664` n `160`; fx avg `-0.0861` n `6`; index avg `0.054` n `27`; metal avg `0.0341` n `20`; unknown avg `1.0859` n `1233`
- 24h: commodity avg `-0.4864` n `13`; crypto_alt avg `1.7265` n `239`; crypto_major avg `0.6779` n `8`; equity avg `4.721` n `160`; fx avg `-0.0285` n `6`; index avg `0.5435` n `27`; metal avg `0.1442` n `20`; unknown avg `190.7871` n `1065`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
