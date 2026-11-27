# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T22:07:31.439626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `13`; crypto_alt avg `-0.1875` n `239`; crypto_major avg `-0.2919` n `8`; equity avg `-0.0659` n `168`; fx avg `-0.0003` n `6`; index avg `-0.0001` n `27`; metal avg `-0.0074` n `20`; unknown avg `-0.3519` n `1245`
- 1h: commodity avg `0.0016` n `13`; crypto_alt avg `-0.1504` n `239`; crypto_major avg `-0.432` n `8`; equity avg `-0.1254` n `168`; fx avg `-0.0009` n `6`; index avg `0.0142` n `27`; metal avg `-0.0221` n `20`; unknown avg `0.9317` n `1189`
- 4h: commodity avg `0.0416` n `13`; crypto_alt avg `-0.1475` n `239`; crypto_major avg `-0.4094` n `8`; equity avg `-0.2831` n `168`; fx avg `-0.0004` n `6`; index avg `0.0107` n `27`; metal avg `0.1004` n `20`; unknown avg `179.5857` n `1160`
- 24h: commodity avg `-0.4634` n `13`; crypto_alt avg `-0.0639` n `239`; crypto_major avg `-0.1926` n `8`; equity avg `3.0173` n `168`; fx avg `-0.1496` n `6`; index avg `0.3192` n `27`; metal avg `0.9416` n `20`; unknown avg `273.9487` n `1001`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
