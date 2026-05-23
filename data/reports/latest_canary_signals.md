# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T17:52:32.106622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `12`; crypto_alt avg `-0.0935` n `228`; crypto_major avg `0.0335` n `8`; equity avg `-0.0546` n `67`; fx avg `0.0022` n `6`; index avg `-0.0404` n `23`; metal avg `-0.0003` n `18`; unknown avg `-0.1329` n `396`
- 1h: commodity avg `0.1439` n `12`; crypto_alt avg `0.0086` n `228`; crypto_major avg `-0.0956` n `8`; equity avg `-0.0443` n `67`; fx avg `-0.0007` n `6`; index avg `-0.0131` n `23`; metal avg `0.0294` n `18`; unknown avg `-0.4306` n `396`
- 4h: commodity avg `-0.5777` n `12`; crypto_alt avg `1.5621` n `228`; crypto_major avg `1.1123` n `8`; equity avg `0.5893` n `67`; fx avg `0.0086` n `6`; index avg `0.1108` n `23`; metal avg `0.2143` n `18`; unknown avg `0.6973` n `396`
- 24h: commodity avg `0.5095` n `12`; crypto_alt avg `-2.804` n `228`; crypto_major avg `-1.9068` n `8`; equity avg `-0.8743` n `67`; fx avg `0.0162` n `6`; index avg `-0.3276` n `23`; metal avg `-0.2279` n `18`; unknown avg `-2.0399` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
