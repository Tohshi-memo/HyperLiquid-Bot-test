# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T01:22:30.895583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0735` n `12`; crypto_alt avg `0.2456` n `228`; crypto_major avg `0.3327` n `8`; equity avg `0.0217` n `78`; fx avg `0.0107` n `6`; index avg `0.0284` n `23`; metal avg `-0.1189` n `18`; unknown avg `0.174` n `702`
- 1h: commodity avg `-0.2994` n `12`; crypto_alt avg `0.9262` n `228`; crypto_major avg `0.9122` n `8`; equity avg `0.4922` n `78`; fx avg `0.0793` n `6`; index avg `0.2256` n `23`; metal avg `0.5534` n `18`; unknown avg `1.6589` n `694`
- 4h: commodity avg `-0.3401` n `12`; crypto_alt avg `0.8338` n `228`; crypto_major avg `0.7` n `8`; equity avg `-0.3873` n `78`; fx avg `0.1409` n `6`; index avg `0.0587` n `23`; metal avg `0.7235` n `18`; unknown avg `1.4262` n `694`
- 24h: commodity avg `-0.2276` n `12`; crypto_alt avg `0.3188` n `228`; crypto_major avg `-0.3982` n `8`; equity avg `-0.4154` n `78`; fx avg `0.0368` n `6`; index avg `0.0574` n `23`; metal avg `0.5883` n `18`; unknown avg `1.2093` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
