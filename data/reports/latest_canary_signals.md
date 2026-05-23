# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T13:22:14.666217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `0.2239` n `228`; crypto_major avg `0.1898` n `8`; equity avg `0.0861` n `67`; fx avg `0.0006` n `6`; index avg `0.0242` n `23`; metal avg `0.0432` n `18`; unknown avg `0.0696` n `396`
- 1h: commodity avg `0.1647` n `12`; crypto_alt avg `1.2078` n `228`; crypto_major avg `0.7075` n `8`; equity avg `0.2449` n `67`; fx avg `0.0021` n `6`; index avg `0.143` n `23`; metal avg `0.032` n `18`; unknown avg `-0.1343` n `396`
- 4h: commodity avg `0.0453` n `12`; crypto_alt avg `1.0316` n `228`; crypto_major avg `0.6119` n `8`; equity avg `0.2991` n `67`; fx avg `0.0056` n `6`; index avg `0.1969` n `23`; metal avg `-0.0017` n `18`; unknown avg `-0.3939` n `396`
- 24h: commodity avg `0.7001` n `12`; crypto_alt avg `-5.4305` n `228`; crypto_major avg `-4.0319` n `8`; equity avg `-1.7905` n `67`; fx avg `0.0587` n `6`; index avg `-0.1575` n `23`; metal avg `-0.6744` n `18`; unknown avg `-2.8301` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
