# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T13:07:22.263350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2245` n `12`; crypto_alt avg `0.2293` n `228`; crypto_major avg `0.1575` n `8`; equity avg `-0.0692` n `67`; fx avg `-0.0001` n `6`; index avg `-0.0154` n `23`; metal avg `0.1061` n `18`; unknown avg `0.0622` n `418`
- 1h: commodity avg `0.4972` n `12`; crypto_alt avg `0.1199` n `228`; crypto_major avg `0.0536` n `8`; equity avg `-0.0921` n `67`; fx avg `0.0095` n `6`; index avg `-0.0158` n `23`; metal avg `-0.0263` n `18`; unknown avg `-0.7013` n `417`
- 4h: commodity avg `-0.1992` n `12`; crypto_alt avg `1.4699` n `228`; crypto_major avg `1.387` n `8`; equity avg `0.2619` n `67`; fx avg `-0.0081` n `6`; index avg `0.2553` n `23`; metal avg `0.1739` n `18`; unknown avg `0.4975` n `417`
- 24h: commodity avg `0.3847` n `12`; crypto_alt avg `0.4425` n `228`; crypto_major avg `-0.3918` n `8`; equity avg `-0.3574` n `67`; fx avg `-0.1426` n `6`; index avg `0.0909` n `23`; metal avg `-0.5307` n `18`; unknown avg `-0.1118` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1857`, n `670`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1807`, n `670`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.171`, n `670`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1707`, n `670`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1476`, n `670`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1328`, n `670`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1314`, n `670`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1302`, n `670`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1297`, n `670`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.127`, n `670`, weak_sample_signal
