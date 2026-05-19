# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T01:52:16.720365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0323` n `12`; crypto_alt avg `-0.0998` n `228`; crypto_major avg `-0.2527` n `8`; equity avg `-0.0663` n `66`; fx avg `-0.0045` n `6`; index avg `0.0048` n `23`; metal avg `0.0614` n `18`; unknown avg `-0.1654` n `383`
- 1h: commodity avg `0.1416` n `12`; crypto_alt avg `-0.5689` n `228`; crypto_major avg `-0.6939` n `8`; equity avg `-0.4927` n `66`; fx avg `0.0375` n `6`; index avg `-0.2256` n `23`; metal avg `-0.2899` n `18`; unknown avg `-0.1467` n `383`
- 4h: commodity avg `0.0981` n `12`; crypto_alt avg `0.1268` n `228`; crypto_major avg `-0.349` n `8`; equity avg `-0.3026` n `66`; fx avg `0.1256` n `6`; index avg `-0.3477` n `23`; metal avg `-0.2002` n `18`; unknown avg `-0.6089` n `383`
- 24h: commodity avg `0.1069` n `12`; crypto_alt avg `1.232` n `228`; crypto_major avg `0.2033` n `8`; equity avg `-0.6275` n `66`; fx avg `0.2259` n `6`; index avg `-0.0935` n `23`; metal avg `1.1699` n `18`; unknown avg `0.1129` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1828`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1554`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
