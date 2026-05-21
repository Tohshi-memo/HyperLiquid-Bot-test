# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T17:52:17.221507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.41` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.8725` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `2.7217` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.6854` n `12`; crypto_alt avg `0.279` n `228`; crypto_major avg `0.0492` n `8`; equity avg `0.3064` n `67`; fx avg `0.0055` n `6`; index avg `0.1758` n `23`; metal avg `0.2405` n `18`; unknown avg `-0.083` n `386`
- 1h: commodity avg `-1.5149` n `12`; crypto_alt avg `1.6155` n `228`; crypto_major avg `1.2068` n `8`; equity avg `1.1592` n `67`; fx avg `0.0074` n `6`; index avg `0.7051` n `23`; metal avg `0.9217` n `18`; unknown avg `2.5362` n `385`
- 4h: commodity avg `-1.5624` n `12`; crypto_alt avg `1.9972` n `228`; crypto_major avg `1.3101` n `8`; equity avg `1.3235` n `67`; fx avg `0.0109` n `6`; index avg `0.4939` n `23`; metal avg `1.3974` n `18`; unknown avg `2.5362` n `385`
- 24h: commodity avg `-0.7822` n `12`; crypto_alt avg `2.2974` n `228`; crypto_major avg `2.5584` n `8`; equity avg `2.0054` n `66`; fx avg `0.011` n `6`; index avg `0.8858` n `23`; metal avg `0.7696` n `18`; unknown avg `7.5625` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0487`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
