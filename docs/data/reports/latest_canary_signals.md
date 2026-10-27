# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T21:22:30.770814+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `13`; crypto_alt avg `-0.2188` n `238`; crypto_major avg `-0.1754` n `8`; equity avg `-0.0274` n `154`; fx avg `0.0031` n `6`; index avg `-0.0012` n `27`; metal avg `0.008` n `20`; unknown avg `1.2891` n `1236`
- 1h: commodity avg `-0.0102` n `13`; crypto_alt avg `-0.2621` n `238`; crypto_major avg `-0.1964` n `8`; equity avg `-0.0702` n `154`; fx avg `0.0019` n `6`; index avg `-0.0019` n `27`; metal avg `0.024` n `20`; unknown avg `2.2001` n `1222`
- 4h: commodity avg `0.1051` n `13`; crypto_alt avg `-0.1251` n `238`; crypto_major avg `-0.2136` n `8`; equity avg `-0.26` n `154`; fx avg `-0.0132` n `6`; index avg `0.0047` n `27`; metal avg `0.037` n `20`; unknown avg `2.2697` n `1152`
- 24h: commodity avg `-0.2249` n `13`; crypto_alt avg `1.1988` n `237`; crypto_major avg `1.3879` n `8`; equity avg `1.4553` n `154`; fx avg `-0.0424` n `6`; index avg `0.4091` n `27`; metal avg `0.2208` n `20`; unknown avg `26.3819` n `1042`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2331`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2006`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1994`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
