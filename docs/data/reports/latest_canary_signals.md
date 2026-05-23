# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T12:06:11.909244+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1399` n `12`; crypto_alt avg `-0.1444` n `228`; crypto_major avg `-0.0755` n `8`; equity avg `0.0184` n `67`; fx avg `0.0036` n `6`; index avg `0.011` n `23`; metal avg `0.0146` n `18`; unknown avg `-0.0362` n `396`
- 1h: commodity avg `-0.1275` n `12`; crypto_alt avg `-0.3807` n `228`; crypto_major avg `-0.1384` n `8`; equity avg `-0.0122` n `67`; fx avg `-0.0046` n `6`; index avg `0.1112` n `23`; metal avg `0.0446` n `18`; unknown avg `0.9219` n `396`
- 4h: commodity avg `-0.028` n `12`; crypto_alt avg `0.4776` n `228`; crypto_major avg `0.2129` n `8`; equity avg `0.2824` n `67`; fx avg `-0.0055` n `6`; index avg `0.0702` n `23`; metal avg `-0.0012` n `18`; unknown avg `0.1582` n `386`
- 24h: commodity avg `-0.0162` n `12`; crypto_alt avg `-6.2402` n `228`; crypto_major avg `-4.468` n `8`; equity avg `-1.6493` n `67`; fx avg `0.0565` n `6`; index avg `-0.0758` n `23`; metal avg `-0.7703` n `18`; unknown avg `-1.5112` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
