# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T13:22:27.888633+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1262` n `12`; crypto_alt avg `0.3184` n `228`; crypto_major avg `0.0966` n `8`; equity avg `0.1806` n `72`; fx avg `-0.0063` n `6`; index avg `0.0643` n `23`; metal avg `-0.2269` n `18`; unknown avg `0.0456` n `420`
- 1h: commodity avg `-0.5868` n `12`; crypto_alt avg `0.6892` n `228`; crypto_major avg `0.2528` n `8`; equity avg `-0.0907` n `72`; fx avg `0.0063` n `6`; index avg `-0.0313` n `23`; metal avg `-0.2487` n `18`; unknown avg `-0.0721` n `420`
- 4h: commodity avg `-0.7612` n `12`; crypto_alt avg `1.0917` n `228`; crypto_major avg `0.1369` n `8`; equity avg `0.0395` n `72`; fx avg `-0.0197` n `6`; index avg `-0.0598` n `23`; metal avg `-0.2687` n `18`; unknown avg `-0.3889` n `420`
- 24h: commodity avg `1.2172` n `12`; crypto_alt avg `-0.9775` n `228`; crypto_major avg `-3.2726` n `8`; equity avg `0.479` n `72`; fx avg `-0.0098` n `6`; index avg `0.7985` n `23`; metal avg `-1.3804` n `18`; unknown avg `-0.3613` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
