# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T19:52:33.947484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.028` n `12`; crypto_alt avg `-0.2205` n `228`; crypto_major avg `-0.1186` n `8`; equity avg `-0.0335` n `74`; fx avg `0.0069` n `6`; index avg `0.0183` n `23`; metal avg `0.0427` n `18`; unknown avg `0.1627` n `645`
- 1h: commodity avg `-0.0018` n `12`; crypto_alt avg `0.1182` n `228`; crypto_major avg `0.034` n `8`; equity avg `0.0075` n `74`; fx avg `0.0178` n `6`; index avg `0.0064` n `23`; metal avg `-0.0272` n `18`; unknown avg `0.5134` n `645`
- 4h: commodity avg `0.0257` n `12`; crypto_alt avg `-0.0172` n `228`; crypto_major avg `-0.0984` n `8`; equity avg `-0.1371` n `74`; fx avg `0.0045` n `6`; index avg `-0.0499` n `23`; metal avg `0.0173` n `18`; unknown avg `0.296` n `645`
- 24h: commodity avg `0.1221` n `12`; crypto_alt avg `-1.5203` n `228`; crypto_major avg `-0.7393` n `8`; equity avg `0.2155` n `74`; fx avg `-0.035` n `6`; index avg `0.2224` n `23`; metal avg `0.0745` n `18`; unknown avg `1.4509` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
