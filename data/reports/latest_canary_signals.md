# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T22:37:25.862781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `0.0911` n `229`; crypto_major avg `0.0778` n `8`; equity avg `0.0105` n `92`; fx avg `-0.0261` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0044` n `20`; unknown avg `0.0131` n `765`
- 1h: commodity avg `0.0156` n `12`; crypto_alt avg `0.1129` n `229`; crypto_major avg `0.0189` n `8`; equity avg `0.0006` n `92`; fx avg `-0.0297` n `6`; index avg `-0.0009` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.0807` n `765`
- 4h: commodity avg `-0.0333` n `12`; crypto_alt avg `0.4211` n `229`; crypto_major avg `0.1825` n `8`; equity avg `-0.1037` n `92`; fx avg `-0.0307` n `6`; index avg `0.0054` n `25`; metal avg `0.0874` n `20`; unknown avg `-0.4084` n `765`
- 24h: commodity avg `-0.2357` n `12`; crypto_alt avg `1.169` n `229`; crypto_major avg `0.9344` n `8`; equity avg `-0.7051` n `92`; fx avg `-0.1938` n `6`; index avg `0.0366` n `25`; metal avg `0.1472` n `20`; unknown avg `-0.3063` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
