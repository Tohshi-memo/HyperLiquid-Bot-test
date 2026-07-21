# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T11:37:25.350939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `0.1022` n `230`; crypto_major avg `0.1401` n `8`; equity avg `0.1029` n `98`; fx avg `-0.0024` n `6`; index avg `0.0141` n `25`; metal avg `0.0177` n `20`; unknown avg `-0.0346` n `771`
- 1h: commodity avg `0.143` n `12`; crypto_alt avg `-0.1061` n `230`; crypto_major avg `-0.1434` n `8`; equity avg `-0.2283` n `98`; fx avg `-0.0128` n `6`; index avg `-0.0205` n `25`; metal avg `-0.0897` n `20`; unknown avg `0.0261` n `771`
- 4h: commodity avg `0.2786` n `12`; crypto_alt avg `-0.1309` n `230`; crypto_major avg `0.0343` n `8`; equity avg `0.2082` n `98`; fx avg `-0.0007` n `6`; index avg `0.0433` n `25`; metal avg `-0.0971` n `20`; unknown avg `0.0289` n `771`
- 24h: commodity avg `0.8289` n `12`; crypto_alt avg `1.6574` n `230`; crypto_major avg `1.7066` n `8`; equity avg `0.8765` n `98`; fx avg `-0.0675` n `6`; index avg `0.1081` n `25`; metal avg `0.4496` n `20`; unknown avg `0.1012` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0872`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0672`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0667`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
