# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T23:37:31.671591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `13`; crypto_alt avg `0.1847` n `239`; crypto_major avg `0.0088` n `8`; equity avg `-0.3184` n `166`; fx avg `-0.0084` n `6`; index avg `-0.0778` n `27`; metal avg `-0.0333` n `20`; unknown avg `355.4908` n `1266`
- 1h: commodity avg `0.0047` n `13`; crypto_alt avg `0.7044` n `239`; crypto_major avg `0.2808` n `8`; equity avg `-0.4449` n `166`; fx avg `-0.0107` n `6`; index avg `-0.0955` n `27`; metal avg `-0.0255` n `20`; unknown avg `0.1528` n `1258`
- 4h: commodity avg `0.0979` n `13`; crypto_alt avg `-0.3163` n `239`; crypto_major avg `-0.2309` n `8`; equity avg `0.3493` n `166`; fx avg `0.0049` n `6`; index avg `0.0041` n `27`; metal avg `-0.0312` n `20`; unknown avg `330.3006` n `1212`
- 24h: commodity avg `-1.0936` n `13`; crypto_alt avg `0.9441` n `239`; crypto_major avg `0.7395` n `8`; equity avg `5.512` n `166`; fx avg `-0.2091` n `6`; index avg `0.5385` n `27`; metal avg `0.2386` n `20`; unknown avg `97.3439` n `1047`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
