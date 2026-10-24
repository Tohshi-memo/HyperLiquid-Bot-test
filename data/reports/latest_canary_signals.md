# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T18:52:24.256243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `13`; crypto_alt avg `0.267` n `237`; crypto_major avg `0.2118` n `8`; equity avg `0.1361` n `152`; fx avg `-0.0041` n `6`; index avg `0.0046` n `26`; metal avg `0.0012` n `20`; unknown avg `0.9982` n `1231`
- 1h: commodity avg `-0.0266` n `13`; crypto_alt avg `0.6007` n `237`; crypto_major avg `0.3941` n `8`; equity avg `0.1753` n `152`; fx avg `0.004` n `6`; index avg `0.0102` n `26`; metal avg `0.0036` n `20`; unknown avg `0.6015` n `1231`
- 4h: commodity avg `-0.0271` n `13`; crypto_alt avg `0.3634` n `237`; crypto_major avg `0.2986` n `8`; equity avg `0.1045` n `152`; fx avg `-0.0116` n `6`; index avg `0.0048` n `26`; metal avg `-0.0129` n `20`; unknown avg `0.0085` n `1200`
- 24h: commodity avg `0.1389` n `13`; crypto_alt avg `-3.2244` n `237`; crypto_major avg `-2.0994` n `8`; equity avg `-0.6183` n `152`; fx avg `-0.0287` n `6`; index avg `-0.0678` n `26`; metal avg `-0.2051` n `20`; unknown avg `-0.8037` n `1046`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1909`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1825`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
