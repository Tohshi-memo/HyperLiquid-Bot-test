# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T14:07:29.440743+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `13`; crypto_alt avg `-0.0348` n `237`; crypto_major avg `0.0014` n `8`; equity avg `-0.0036` n `152`; fx avg `-0.0085` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0007` n `20`; unknown avg `-0.1418` n `1228`
- 1h: commodity avg `-0.0315` n `13`; crypto_alt avg `-0.3155` n `237`; crypto_major avg `-0.0827` n `8`; equity avg `-0.05` n `152`; fx avg `-0.0134` n `6`; index avg `-0.0128` n `26`; metal avg `0.0003` n `20`; unknown avg `0.8128` n `1198`
- 4h: commodity avg `0.0964` n `13`; crypto_alt avg `-0.2659` n `237`; crypto_major avg `0.2864` n `8`; equity avg `0.1358` n `152`; fx avg `-0.0209` n `6`; index avg `0.0034` n `26`; metal avg `0.019` n `20`; unknown avg `1.3478` n `1190`
- 24h: commodity avg `0.2557` n `13`; crypto_alt avg `-3.0239` n `237`; crypto_major avg `-2.2505` n `8`; equity avg `-0.4018` n `152`; fx avg `-0.0344` n `6`; index avg `-0.0008` n `26`; metal avg `-0.1201` n `20`; unknown avg `-0.2713` n `1043`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1914`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
