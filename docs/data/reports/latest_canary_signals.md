# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T13:22:32.595119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0346` n `13`; crypto_alt avg `-0.0329` n `237`; crypto_major avg `-0.0322` n `8`; equity avg `-0.1494` n `152`; fx avg `0.0014` n `6`; index avg `-0.0264` n `26`; metal avg `-0.0339` n `20`; unknown avg `0.3673` n `1236`
- 1h: commodity avg `0.0681` n `13`; crypto_alt avg `-0.0382` n `237`; crypto_major avg `-0.1618` n `8`; equity avg `-0.3987` n `152`; fx avg `-0.0126` n `6`; index avg `-0.0712` n `26`; metal avg `-0.1044` n `20`; unknown avg `39.1732` n `1222`
- 4h: commodity avg `0.2175` n `13`; crypto_alt avg `0.0375` n `237`; crypto_major avg `0.041` n `8`; equity avg `0.1846` n `152`; fx avg `-0.0038` n `6`; index avg `-0.0097` n `26`; metal avg `-0.0545` n `20`; unknown avg `10.5876` n `1216`
- 24h: commodity avg `-0.2705` n `13`; crypto_alt avg `0.2402` n `237`; crypto_major avg `0.1529` n `8`; equity avg `-0.2712` n `152`; fx avg `0.0367` n `6`; index avg `0.0136` n `26`; metal avg `0.089` n `20`; unknown avg `0.1975` n `959`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2472`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2055`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
