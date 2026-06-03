# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T13:52:28.035934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0258` n `12`; crypto_alt avg `0.113` n `228`; crypto_major avg `-0.0698` n `8`; equity avg `-0.5704` n `72`; fx avg `-0.0233` n `6`; index avg `-0.4292` n `23`; metal avg `-0.2986` n `18`; unknown avg `0.8008` n `420`
- 1h: commodity avg `-0.5721` n `12`; crypto_alt avg `0.256` n `228`; crypto_major avg `-0.3835` n `8`; equity avg `-1.6286` n `72`; fx avg `-0.008` n `6`; index avg `-0.6887` n `23`; metal avg `-0.6474` n `18`; unknown avg `1.0593` n `420`
- 4h: commodity avg `-1.0236` n `12`; crypto_alt avg `0.6521` n `228`; crypto_major avg `-0.5134` n `8`; equity avg `-1.5108` n `72`; fx avg `-0.0571` n `6`; index avg `-0.7564` n `23`; metal avg `-0.5485` n `18`; unknown avg `-0.1098` n `420`
- 24h: commodity avg `0.8445` n `12`; crypto_alt avg `-0.7143` n `228`; crypto_major avg `-3.4407` n `8`; equity avg `-0.965` n `72`; fx avg `0.0244` n `6`; index avg `-0.1113` n `23`; metal avg `-1.814` n `18`; unknown avg `-0.1966` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0425`, n `668`, weak_sample_signal
