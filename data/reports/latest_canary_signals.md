# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T12:22:21.772238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1462` n `12`; crypto_alt avg `-0.2646` n `228`; crypto_major avg `-0.1798` n `8`; equity avg `0.0944` n `72`; fx avg `-0.0251` n `6`; index avg `-0.0525` n `23`; metal avg `-0.0757` n `18`; unknown avg `0.8294` n `420`
- 1h: commodity avg `-0.0382` n `12`; crypto_alt avg `-0.9101` n `228`; crypto_major avg `-0.7687` n `8`; equity avg `-0.1732` n `72`; fx avg `-0.0611` n `6`; index avg `-0.0687` n `23`; metal avg `-0.0972` n `18`; unknown avg `-0.2581` n `420`
- 4h: commodity avg `-0.0773` n `12`; crypto_alt avg `0.1198` n `228`; crypto_major avg `-0.1594` n `8`; equity avg `-0.0198` n `72`; fx avg `-0.0264` n `6`; index avg `-0.0265` n `23`; metal avg `0.1477` n `18`; unknown avg `-0.323` n `420`
- 24h: commodity avg `1.8279` n `12`; crypto_alt avg `-1.0953` n `228`; crypto_major avg `-3.4487` n `8`; equity avg `0.4382` n `72`; fx avg `-0.0092` n `6`; index avg `0.7849` n `23`; metal avg `-1.5241` n `18`; unknown avg `0.6269` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0433`, n `668`, weak_sample_signal
