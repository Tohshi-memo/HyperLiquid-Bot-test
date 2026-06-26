# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T15:22:26.744561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0515` n `12`; crypto_alt avg `0.2931` n `228`; crypto_major avg `0.3282` n `8`; equity avg `0.2813` n `86`; fx avg `0.0071` n `6`; index avg `0.0345` n `23`; metal avg `0.0522` n `20`; unknown avg `-0.064` n `765`
- 1h: commodity avg `-0.1575` n `12`; crypto_alt avg `0.1288` n `228`; crypto_major avg `-0.11` n `8`; equity avg `-0.3642` n `86`; fx avg `-0.0357` n `6`; index avg `-0.0891` n `23`; metal avg `-0.112` n `20`; unknown avg `-0.0592` n `765`
- 4h: commodity avg `-0.2817` n `12`; crypto_alt avg `1.3574` n `228`; crypto_major avg `1.4904` n `8`; equity avg `0.9891` n `86`; fx avg `-0.0453` n `6`; index avg `0.0842` n `23`; metal avg `0.2864` n `20`; unknown avg `0.1729` n `765`
- 24h: commodity avg `-0.5507` n `12`; crypto_alt avg `1.8107` n `228`; crypto_major avg `2.6276` n `8`; equity avg `-0.6313` n `86`; fx avg `-0.0326` n `6`; index avg `-0.2427` n `23`; metal avg `0.4655` n `20`; unknown avg `0.1186` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.3353`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1829`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
