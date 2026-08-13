# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T17:38:02.366801+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0397` n `12`; crypto_alt avg `-0.0246` n `230`; crypto_major avg `0.0259` n `8`; equity avg `-0.0657` n `113`; fx avg `0.004` n `6`; index avg `-0.0138` n `25`; metal avg `-0.0291` n `20`; unknown avg `-0.0735` n `787`
- 1h: commodity avg `-0.1373` n `12`; crypto_alt avg `-0.0094` n `230`; crypto_major avg `0.0958` n `8`; equity avg `0.2513` n `113`; fx avg `0.0043` n `6`; index avg `0.0373` n `25`; metal avg `0.0091` n `20`; unknown avg `0.0437` n `787`
- 4h: commodity avg `0.1183` n `12`; crypto_alt avg `-0.6025` n `230`; crypto_major avg `-0.4203` n `8`; equity avg `0.758` n `113`; fx avg `-0.0106` n `6`; index avg `0.2056` n `25`; metal avg `-0.0363` n `20`; unknown avg `-0.1129` n `787`
- 24h: commodity avg `-0.4232` n `12`; crypto_alt avg `-0.8677` n `230`; crypto_major avg `-0.2671` n `8`; equity avg `1.4541` n `113`; fx avg `-0.006` n `6`; index avg `0.3425` n `25`; metal avg `-0.4276` n `20`; unknown avg `0.0809` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2353`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1909`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1881`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
