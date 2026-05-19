# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T01:22:13.812181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.075` n `12`; crypto_alt avg `-0.2894` n `228`; crypto_major avg `-0.3512` n `8`; equity avg `-0.4471` n `66`; fx avg `0.0084` n `6`; index avg `-0.1601` n `23`; metal avg `-0.3219` n `18`; unknown avg `0.863` n `383`
- 1h: commodity avg `0.2195` n `12`; crypto_alt avg `-0.5732` n `228`; crypto_major avg `-0.6478` n `8`; equity avg `-0.8506` n `66`; fx avg `0.0561` n `6`; index avg `-0.4008` n `23`; metal avg `-0.8695` n `18`; unknown avg `0.8752` n `383`
- 4h: commodity avg `0.2739` n `12`; crypto_alt avg `0.5367` n `228`; crypto_major avg `0.1286` n `8`; equity avg `-0.4005` n `66`; fx avg `0.1355` n `6`; index avg `-0.2378` n `23`; metal avg `-0.3516` n `18`; unknown avg `-0.3618` n `383`
- 24h: commodity avg `-0.0402` n `12`; crypto_alt avg `1.1641` n `228`; crypto_major avg `0.2863` n `8`; equity avg `-0.392` n `66`; fx avg `0.2623` n `6`; index avg `-0.0754` n `23`; metal avg `1.7061` n `18`; unknown avg `0.3003` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
