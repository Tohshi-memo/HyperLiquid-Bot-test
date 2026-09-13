# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T18:07:25.938608+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.0312` n `233`; crypto_major avg `-0.0639` n `8`; equity avg `-0.0115` n `136`; fx avg `-0.0037` n `6`; index avg `0.0073` n `27`; metal avg `-0.0047` n `20`; unknown avg `0.3008` n `838`
- 1h: commodity avg `0.0069` n `12`; crypto_alt avg `0.1638` n `233`; crypto_major avg `0.0142` n `8`; equity avg `0.0788` n `136`; fx avg `-0.0061` n `6`; index avg `-0.0048` n `27`; metal avg `-0.0085` n `20`; unknown avg `-0.5345` n `800`
- 4h: commodity avg `0.0227` n `12`; crypto_alt avg `0.1227` n `233`; crypto_major avg `0.6291` n `8`; equity avg `0.2849` n `136`; fx avg `-0.0028` n `6`; index avg `-0.0098` n `27`; metal avg `0.0178` n `20`; unknown avg `3.1867` n `774`
- 24h: commodity avg `0.2437` n `12`; crypto_alt avg `0.0572` n `233`; crypto_major avg `-0.814` n `8`; equity avg `-1.4093` n `136`; fx avg `0.0128` n `6`; index avg `-0.2616` n `26`; metal avg `-0.0716` n `20`; unknown avg `1.5527` n `688`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
