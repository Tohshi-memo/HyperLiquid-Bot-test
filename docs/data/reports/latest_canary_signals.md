# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T09:37:28.132747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `0.1811` n `228`; crypto_major avg `0.1927` n `8`; equity avg `0.0294` n `78`; fx avg `0.0006` n `6`; index avg `0.0013` n `23`; metal avg `0.0031` n `18`; unknown avg `0.1919` n `702`
- 1h: commodity avg `0.0177` n `12`; crypto_alt avg `0.4174` n `228`; crypto_major avg `0.4731` n `8`; equity avg `0.0581` n `78`; fx avg `-0.0049` n `6`; index avg `0.0106` n `23`; metal avg `0.0139` n `18`; unknown avg `0.172` n `702`
- 4h: commodity avg `-0.0637` n `12`; crypto_alt avg `0.4765` n `228`; crypto_major avg `-0.1459` n `8`; equity avg `0.045` n `78`; fx avg `-0.011` n `6`; index avg `0.0094` n `23`; metal avg `0.0269` n `18`; unknown avg `0.0243` n `662`
- 24h: commodity avg `0.0616` n `12`; crypto_alt avg `1.1191` n `228`; crypto_major avg `-0.0628` n `8`; equity avg `0.3676` n `78`; fx avg `0.0377` n `6`; index avg `0.0272` n `23`; metal avg `-0.0103` n `18`; unknown avg `0.2518` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
