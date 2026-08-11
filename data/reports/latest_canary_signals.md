# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T00:22:32.835594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0182` n `12`; crypto_alt avg `0.1373` n `230`; crypto_major avg `0.0887` n `8`; equity avg `0.1582` n `113`; fx avg `-0.0065` n `6`; index avg `0.0284` n `25`; metal avg `0.0636` n `20`; unknown avg `0.0972` n `785`
- 1h: commodity avg `0.0113` n `12`; crypto_alt avg `0.1579` n `230`; crypto_major avg `-0.0622` n `8`; equity avg `0.1447` n `113`; fx avg `-0.0035` n `6`; index avg `-0.0215` n `25`; metal avg `0.1124` n `20`; unknown avg `-0.025` n `785`
- 4h: commodity avg `-0.0397` n `12`; crypto_alt avg `-0.2962` n `230`; crypto_major avg `-0.4186` n `8`; equity avg `-0.1876` n `113`; fx avg `-0.0075` n `6`; index avg `-0.0391` n `25`; metal avg `0.1433` n `20`; unknown avg `-0.1675` n `785`
- 24h: commodity avg `0.7887` n `12`; crypto_alt avg `-0.5993` n `230`; crypto_major avg `-0.7639` n `8`; equity avg `-1.7875` n `113`; fx avg `0.2082` n `6`; index avg `-0.1271` n `25`; metal avg `0.4858` n `20`; unknown avg `103.6904` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
