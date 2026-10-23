# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T01:43:30.150459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0204` n `13`; crypto_alt avg `0.3646` n `237`; crypto_major avg `0.1437` n `8`; equity avg `0.5361` n `151`; fx avg `0.0267` n `6`; index avg `0.0626` n `26`; metal avg `-0.0334` n `20`; unknown avg `0.1742` n `1233`
- 1h: commodity avg `0.1271` n `13`; crypto_alt avg `0.5128` n `237`; crypto_major avg `0.2219` n `8`; equity avg `0.9402` n `151`; fx avg `0.0392` n `6`; index avg `0.1125` n `26`; metal avg `-0.0402` n `20`; unknown avg `0.6978` n `1231`
- 4h: commodity avg `0.1188` n `13`; crypto_alt avg `0.5111` n `237`; crypto_major avg `0.2668` n `8`; equity avg `0.9043` n `151`; fx avg `-0.0498` n `6`; index avg `0.0998` n `26`; metal avg `-0.1243` n `20`; unknown avg `0.2728` n `1185`
- 24h: commodity avg `0.4508` n `13`; crypto_alt avg `-3.7931` n `237`; crypto_major avg `-2.5107` n `8`; equity avg `-3.638` n `151`; fx avg `-0.2129` n `6`; index avg `-0.4166` n `26`; metal avg `-0.8612` n `20`; unknown avg `57.0382` n `905`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
