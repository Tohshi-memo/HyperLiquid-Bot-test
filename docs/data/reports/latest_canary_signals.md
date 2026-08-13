# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T06:52:29.458579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0321` n `12`; crypto_alt avg `0.0525` n `230`; crypto_major avg `0.0815` n `8`; equity avg `-0.0996` n `113`; fx avg `0.0294` n `6`; index avg `-0.0038` n `25`; metal avg `0.0391` n `20`; unknown avg `0.0208` n `787`
- 1h: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.0326` n `230`; crypto_major avg `-0.0608` n `8`; equity avg `-0.3648` n `113`; fx avg `0.0924` n `6`; index avg `-0.0323` n `25`; metal avg `-0.0869` n `20`; unknown avg `-0.131` n `755`
- 4h: commodity avg `0.1582` n `12`; crypto_alt avg `0.4319` n `230`; crypto_major avg `0.6217` n `8`; equity avg `-0.3376` n `113`; fx avg `0.0823` n `6`; index avg `-0.0376` n `25`; metal avg `-0.186` n `20`; unknown avg `0.0149` n `754`
- 24h: commodity avg `-0.0056` n `12`; crypto_alt avg `-0.6106` n `230`; crypto_major avg `0.4882` n `8`; equity avg `2.1554` n `113`; fx avg `0.0262` n `6`; index avg `0.2492` n `25`; metal avg `-0.3783` n `20`; unknown avg `0.0624` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2457`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1927`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1906`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1872`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
