# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T00:07:31.074704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0433` n `12`; crypto_alt avg `-0.1086` n `233`; crypto_major avg `-0.04` n `8`; equity avg `0.1084` n `134`; fx avg `0.003` n `6`; index avg `0.0573` n `26`; metal avg `-0.0016` n `20`; unknown avg `0.6116` n `795`
- 1h: commodity avg `-0.0318` n `12`; crypto_alt avg `0.4287` n `233`; crypto_major avg `0.3009` n `8`; equity avg `0.1214` n `134`; fx avg `0.0211` n `6`; index avg `0.0525` n `26`; metal avg `-0.0622` n `20`; unknown avg `2.3531` n `795`
- 4h: commodity avg `0.0116` n `12`; crypto_alt avg `-1.2844` n `233`; crypto_major avg `-0.6269` n `8`; equity avg `-0.0887` n `134`; fx avg `0.0006` n `6`; index avg `0.0646` n `26`; metal avg `-0.0044` n `20`; unknown avg `1.1791` n `707`
- 24h: commodity avg `0.096` n `12`; crypto_alt avg `-3.1547` n `233`; crypto_major avg `-2.0894` n `8`; equity avg `-0.6404` n `134`; fx avg `0.055` n `6`; index avg `-0.1234` n `26`; metal avg `0.5025` n `20`; unknown avg `1.7049` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
