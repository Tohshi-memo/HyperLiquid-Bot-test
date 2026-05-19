# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T21:52:16.643501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0227` n `12`; crypto_alt avg `-0.1099` n `228`; crypto_major avg `-0.0554` n `8`; equity avg `0.021` n `66`; fx avg `0.0007` n `6`; index avg `0.011` n `23`; metal avg `0.021` n `18`; unknown avg `-0.0411` n `383`
- 1h: commodity avg `-0.0669` n `12`; crypto_alt avg `0.0362` n `228`; crypto_major avg `-0.0358` n `8`; equity avg `0.1173` n `66`; fx avg `-0.0015` n `6`; index avg `0.0856` n `23`; metal avg `0.0903` n `18`; unknown avg `-0.1011` n `383`
- 4h: commodity avg `0.302` n `12`; crypto_alt avg `-0.0437` n `228`; crypto_major avg `-0.2029` n `8`; equity avg `-0.3914` n `66`; fx avg `0.0167` n `6`; index avg `-0.1857` n `23`; metal avg `-0.3749` n `18`; unknown avg `0.9696` n `383`
- 24h: commodity avg `0.9724` n `12`; crypto_alt avg `-0.5518` n `228`; crypto_major avg `-0.6623` n `8`; equity avg `-0.0462` n `66`; fx avg `0.0629` n `6`; index avg `-0.7358` n `23`; metal avg `-2.6837` n `18`; unknown avg `0.6389` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
