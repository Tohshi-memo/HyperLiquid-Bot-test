# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T19:59:31.964204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1425` n `12`; crypto_alt avg `-0.0442` n `228`; crypto_major avg `0.0231` n `8`; equity avg `0.0664` n `67`; fx avg `-0.0281` n `6`; index avg `0.0895` n `23`; metal avg `0.0137` n `18`; unknown avg `0.1187` n `396`
- 1h: commodity avg `-0.1591` n `12`; crypto_alt avg `0.016` n `228`; crypto_major avg `0.0374` n `8`; equity avg `0.095` n `67`; fx avg `-0.0362` n `6`; index avg `0.102` n `23`; metal avg `0.0292` n `18`; unknown avg `-0.0473` n `396`
- 4h: commodity avg `-0.8585` n `12`; crypto_alt avg `1.4648` n `228`; crypto_major avg `1.0024` n `8`; equity avg `0.6417` n `67`; fx avg `-0.0395` n `6`; index avg `0.3341` n `23`; metal avg `0.1589` n `18`; unknown avg `1.2073` n `396`
- 24h: commodity avg `-0.5975` n `12`; crypto_alt avg `0.8492` n `228`; crypto_major avg `0.4571` n `8`; equity avg `0.5984` n `67`; fx avg `-0.0632` n `6`; index avg `0.3901` n `23`; metal avg `0.1463` n `18`; unknown avg `-0.6368` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
