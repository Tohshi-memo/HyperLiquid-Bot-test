# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T01:22:31.303055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0238` n `13`; crypto_alt avg `-0.0413` n `239`; crypto_major avg `0.0152` n `8`; equity avg `0.3024` n `162`; fx avg `-0.0165` n `6`; index avg `0.057` n `27`; metal avg `0.1757` n `20`; unknown avg `-0.1024` n `1260`
- 1h: commodity avg `0.0031` n `13`; crypto_alt avg `-0.0869` n `239`; crypto_major avg `-0.3059` n `8`; equity avg `-0.0179` n `162`; fx avg `-0.0384` n `6`; index avg `0.0386` n `27`; metal avg `0.1871` n `20`; unknown avg `-0.1448` n `1259`
- 4h: commodity avg `-0.1279` n `13`; crypto_alt avg `0.2134` n `239`; crypto_major avg `-0.0035` n `8`; equity avg `1.0729` n `162`; fx avg `-0.0445` n `6`; index avg `0.1584` n `27`; metal avg `0.3138` n `20`; unknown avg `12.7506` n `1213`
- 24h: commodity avg `0.8986` n `13`; crypto_alt avg `-0.4066` n `239`; crypto_major avg `-1.4989` n `8`; equity avg `0.2655` n `162`; fx avg `-0.1434` n `6`; index avg `0.1912` n `27`; metal avg `-0.4698` n `20`; unknown avg `51.1516` n `1121`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
