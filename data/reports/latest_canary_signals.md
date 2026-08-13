# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T07:07:28.865185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0516` n `12`; crypto_alt avg `0.0492` n `230`; crypto_major avg `0.1187` n `8`; equity avg `-0.2245` n `113`; fx avg `-0.0142` n `6`; index avg `-0.0164` n `25`; metal avg `-0.0325` n `20`; unknown avg `0.0525` n `787`
- 1h: commodity avg `-0.06` n `12`; crypto_alt avg `0.0922` n `230`; crypto_major avg `0.0937` n `8`; equity avg `-0.439` n `113`; fx avg `0.0676` n `6`; index avg `-0.0172` n `25`; metal avg `-0.0505` n `20`; unknown avg `-0.0365` n `787`
- 4h: commodity avg `0.123` n `12`; crypto_alt avg `0.3715` n `230`; crypto_major avg `0.6226` n `8`; equity avg `-0.5766` n `113`; fx avg `0.0682` n `6`; index avg `-0.059` n `25`; metal avg `-0.2303` n `20`; unknown avg `0.0675` n `754`
- 24h: commodity avg `-0.1486` n `12`; crypto_alt avg `-0.5755` n `230`; crypto_major avg `0.4156` n `8`; equity avg `1.7939` n `113`; fx avg `-0.0044` n `6`; index avg `0.2288` n `25`; metal avg `-0.3661` n `20`; unknown avg `0.0734` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2459`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1921`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1873`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
