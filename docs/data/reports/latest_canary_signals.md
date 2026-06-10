# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T08:37:27.369967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2011` n `12`; crypto_alt avg `-0.2772` n `228`; crypto_major avg `-0.3127` n `8`; equity avg `-0.0295` n `74`; fx avg `-0.0099` n `6`; index avg `0.0083` n `23`; metal avg `0.0378` n `18`; unknown avg `-0.0668` n `547`
- 1h: commodity avg `-0.1186` n `12`; crypto_alt avg `-0.6639` n `228`; crypto_major avg `-0.7775` n `8`; equity avg `-0.4951` n `74`; fx avg `-0.0524` n `6`; index avg `-0.2502` n `23`; metal avg `-0.3423` n `18`; unknown avg `0.1656` n `547`
- 4h: commodity avg `0.0743` n `12`; crypto_alt avg `0.2514` n `228`; crypto_major avg `-0.1551` n `8`; equity avg `0.2188` n `74`; fx avg `0.0349` n `6`; index avg `-0.0314` n `23`; metal avg `0.3098` n `18`; unknown avg `-0.0453` n `537`
- 24h: commodity avg `-0.39` n `12`; crypto_alt avg `-1.6914` n `228`; crypto_major avg `-3.9298` n `8`; equity avg `-3.9376` n `74`; fx avg `0.0774` n `6`; index avg `-2.1036` n `23`; metal avg `-3.4072` n `18`; unknown avg `-0.0254` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0447`, n `668`, weak_sample_signal
