# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T22:07:26.416083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0313` n `13`; crypto_alt avg `-0.1961` n `238`; crypto_major avg `-0.136` n `8`; equity avg `-0.099` n `154`; fx avg `0.0065` n `6`; index avg `-0.0202` n `27`; metal avg `-0.013` n `20`; unknown avg `0.9791` n `1232`
- 1h: commodity avg `-0.027` n `13`; crypto_alt avg `0.1547` n `238`; crypto_major avg `0.1061` n `8`; equity avg `0.0212` n `154`; fx avg `0.0015` n `6`; index avg `-0.0037` n `27`; metal avg `0.0114` n `20`; unknown avg `0.6239` n `1230`
- 4h: commodity avg `0.1217` n `13`; crypto_alt avg `0.2532` n `238`; crypto_major avg `0.177` n `8`; equity avg `-0.0776` n `154`; fx avg `-0.006` n `6`; index avg `0.0025` n `27`; metal avg `0.0797` n `20`; unknown avg `6.3281` n `1150`
- 24h: commodity avg `-0.2118` n `13`; crypto_alt avg `1.2959` n `237`; crypto_major avg `1.567` n `8`; equity avg `1.3492` n `154`; fx avg `-0.0444` n `6`; index avg `0.3789` n `27`; metal avg `0.2224` n `20`; unknown avg `34.0686` n `1042`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2301`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1937`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
