# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T08:37:22.220566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1019` n `12`; crypto_alt avg `-0.3191` n `228`; crypto_major avg `-0.1157` n `8`; equity avg `-0.1592` n `67`; fx avg `-0.0086` n `6`; index avg `-0.0421` n `23`; metal avg `-0.0995` n `18`; unknown avg `0.7997` n `386`
- 1h: commodity avg `0.0981` n `12`; crypto_alt avg `-0.0399` n `228`; crypto_major avg `0.1493` n `8`; equity avg `0.0863` n `67`; fx avg `0.0321` n `6`; index avg `0.0847` n `23`; metal avg `0.0926` n `18`; unknown avg `1.1744` n `386`
- 4h: commodity avg `0.6917` n `12`; crypto_alt avg `-0.1731` n `228`; crypto_major avg `-0.0353` n `8`; equity avg `-0.0083` n `67`; fx avg `0.0154` n `6`; index avg `0.0545` n `23`; metal avg `-0.3829` n `18`; unknown avg `0.7279` n `376`
- 24h: commodity avg `-0.2113` n `12`; crypto_alt avg `1.3726` n `228`; crypto_major avg `-0.2092` n `8`; equity avg `1.3215` n `67`; fx avg `0.114` n `6`; index avg `0.6797` n `23`; metal avg `0.37` n `18`; unknown avg `2.3107` n `375`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0456`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0448`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0442`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0419`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0392`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0366`, n `668`, weak_sample_signal
