# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T12:37:30.877705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `-0.0419` n `234`; crypto_major avg `0.0525` n `8`; equity avg `-0.0007` n `140`; fx avg `-0.0021` n `6`; index avg `0.002` n `26`; metal avg `0.0079` n `20`; unknown avg `0.1226` n `942`
- 1h: commodity avg `-0.0149` n `12`; crypto_alt avg `0.0835` n `234`; crypto_major avg `0.1143` n `8`; equity avg `0.0047` n `140`; fx avg `-0.0266` n `6`; index avg `0.0155` n `26`; metal avg `0.0026` n `20`; unknown avg `0.1105` n `934`
- 4h: commodity avg `-0.0148` n `12`; crypto_alt avg `0.9705` n `234`; crypto_major avg `0.2158` n `8`; equity avg `0.0021` n `140`; fx avg `0.0021` n `6`; index avg `-0.009` n `26`; metal avg `0.0189` n `20`; unknown avg `1.0616` n `934`
- 24h: commodity avg `0.0175` n `12`; crypto_alt avg `4.0793` n `234`; crypto_major avg `3.7899` n `8`; equity avg `0.7658` n `140`; fx avg `-0.0147` n `6`; index avg `0.0649` n `26`; metal avg `-0.0944` n `20`; unknown avg `2.7085` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1709`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
