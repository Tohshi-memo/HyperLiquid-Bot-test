# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T18:37:28.632385+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0826` n `12`; crypto_alt avg `-0.1389` n `234`; crypto_major avg `-0.2154` n `8`; equity avg `-0.0469` n `140`; fx avg `0.0031` n `6`; index avg `-0.0032` n `26`; metal avg `0.004` n `20`; unknown avg `4.4714` n `942`
- 1h: commodity avg `-0.0233` n `12`; crypto_alt avg `-0.1988` n `234`; crypto_major avg `-0.0921` n `8`; equity avg `0.3027` n `140`; fx avg `0.0115` n `6`; index avg `0.05` n `26`; metal avg `0.1121` n `20`; unknown avg `4.2696` n `940`
- 4h: commodity avg `0.0192` n `12`; crypto_alt avg `-0.7356` n `234`; crypto_major avg `0.233` n `8`; equity avg `0.573` n `140`; fx avg `0.0016` n `6`; index avg `0.1514` n `26`; metal avg `0.0481` n `20`; unknown avg `0.3915` n `928`
- 24h: commodity avg `-1.0131` n `12`; crypto_alt avg `3.645` n `234`; crypto_major avg `5.0917` n `8`; equity avg `2.915` n `140`; fx avg `-0.0864` n `6`; index avg `0.6217` n `26`; metal avg `0.06` n `20`; unknown avg `4.2474` n `747`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
