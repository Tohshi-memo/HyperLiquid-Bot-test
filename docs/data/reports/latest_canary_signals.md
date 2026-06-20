# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T17:52:27.501108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `0.2174` n `228`; crypto_major avg `0.1608` n `8`; equity avg `0.0024` n `78`; fx avg `0.1425` n `6`; index avg `0.0231` n `23`; metal avg `-0.0171` n `18`; unknown avg `0.2864` n `701`
- 1h: commodity avg `-0.0474` n `12`; crypto_alt avg `-0.4575` n `228`; crypto_major avg `-0.3775` n `8`; equity avg `-0.0861` n `78`; fx avg `-0.0044` n `6`; index avg `0.0042` n `23`; metal avg `-0.0422` n `18`; unknown avg `-0.1192` n `701`
- 4h: commodity avg `-0.0581` n `12`; crypto_alt avg `0.4639` n `228`; crypto_major avg `0.0943` n `8`; equity avg `0.1118` n `78`; fx avg `0.0565` n `6`; index avg `0.0099` n `23`; metal avg `-0.0239` n `18`; unknown avg `0.242` n `701`
- 24h: commodity avg `0.3524` n `12`; crypto_alt avg `0.0802` n `228`; crypto_major avg `0.6717` n `8`; equity avg `0.3116` n `78`; fx avg `0.0361` n `6`; index avg `0.0695` n `23`; metal avg `0.0932` n `18`; unknown avg `-0.0197` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
