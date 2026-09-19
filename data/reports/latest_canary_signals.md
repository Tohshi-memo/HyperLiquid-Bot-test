# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T23:29:47.392018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0337` n `12`; crypto_alt avg `-0.1184` n `234`; crypto_major avg `0.0225` n `8`; equity avg `-0.0305` n `140`; fx avg `-0.0227` n `6`; index avg `-0.0071` n `26`; metal avg `-0.0102` n `20`; unknown avg `0.111` n `943`
- 1h: commodity avg `0.0316` n `12`; crypto_alt avg `0.7389` n `234`; crypto_major avg `0.6108` n `8`; equity avg `-0.0233` n `140`; fx avg `-0.0209` n `6`; index avg `-0.0099` n `26`; metal avg `-0.0108` n `20`; unknown avg `6.167` n `941`
- 4h: commodity avg `0.0487` n `12`; crypto_alt avg `-0.2539` n `234`; crypto_major avg `-0.5762` n `8`; equity avg `0.0268` n `140`; fx avg `-0.0486` n `6`; index avg `0.0009` n `26`; metal avg `-0.0133` n `20`; unknown avg `4.4261` n `911`
- 24h: commodity avg `0.1053` n `12`; crypto_alt avg `0.868` n `234`; crypto_major avg `-0.1984` n `8`; equity avg `-0.0314` n `140`; fx avg `-0.0978` n `6`; index avg `0.0149` n `26`; metal avg `-0.0318` n `20`; unknown avg `1.9732` n `838`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
