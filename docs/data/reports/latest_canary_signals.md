# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T08:52:33.116670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0101` n `13`; crypto_alt avg `0.285` n `237`; crypto_major avg `0.1061` n `8`; equity avg `0.1297` n `152`; fx avg `-0.0089` n `6`; index avg `0.0259` n `26`; metal avg `0.0192` n `20`; unknown avg `0.1178` n `1240`
- 1h: commodity avg `-0.0256` n `13`; crypto_alt avg `1.0004` n `237`; crypto_major avg `0.4876` n `8`; equity avg `0.2288` n `152`; fx avg `0.0141` n `6`; index avg `0.073` n `26`; metal avg `0.0858` n `20`; unknown avg `0.4258` n `1150`
- 4h: commodity avg `0.1312` n `13`; crypto_alt avg `0.4776` n `237`; crypto_major avg `0.3078` n `8`; equity avg `-0.1029` n `152`; fx avg `0.0041` n `6`; index avg `-0.0173` n `26`; metal avg `-0.0051` n `20`; unknown avg `4.5221` n `1126`
- 24h: commodity avg `-0.484` n `13`; crypto_alt avg `0.7588` n `237`; crypto_major avg `0.3057` n `8`; equity avg `-0.2846` n `152`; fx avg `0.0398` n `6`; index avg `0.0285` n `26`; metal avg `0.2069` n `20`; unknown avg `-0.0737` n `953`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.253`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2071`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1992`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
