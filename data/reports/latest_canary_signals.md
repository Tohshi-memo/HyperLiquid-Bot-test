# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T22:22:24.744187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `12`; crypto_alt avg `0.0403` n `230`; crypto_major avg `0.1023` n `8`; equity avg `0.0019` n `113`; fx avg `0.0025` n `6`; index avg `0.0056` n `25`; metal avg `-0.0017` n `20`; unknown avg `0.0119` n `787`
- 1h: commodity avg `-0.0267` n `12`; crypto_alt avg `0.1532` n `230`; crypto_major avg `0.1479` n `8`; equity avg `0.0907` n `113`; fx avg `0.0006` n `6`; index avg `0.0126` n `25`; metal avg `-0.0369` n `20`; unknown avg `0.1412` n `787`
- 4h: commodity avg `-0.0619` n `12`; crypto_alt avg `0.4239` n `230`; crypto_major avg `0.4038` n `8`; equity avg `0.1172` n `113`; fx avg `0.0049` n `6`; index avg `0.0314` n `25`; metal avg `-0.1025` n `20`; unknown avg `0.2699` n `787`
- 24h: commodity avg `-0.4556` n `12`; crypto_alt avg `0.8434` n `230`; crypto_major avg `0.7996` n `8`; equity avg `1.8041` n `113`; fx avg `0.0237` n `6`; index avg `0.3424` n `25`; metal avg `-0.4488` n `20`; unknown avg `0.1866` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.241`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1975`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
