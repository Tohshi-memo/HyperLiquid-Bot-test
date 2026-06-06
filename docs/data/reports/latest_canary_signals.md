# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T11:22:23.682713+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0632` n `12`; crypto_alt avg `-0.2609` n `228`; crypto_major avg `-0.1013` n `8`; equity avg `0.0866` n `74`; fx avg `-0.0044` n `6`; index avg `-0.0634` n `23`; metal avg `-0.0011` n `18`; unknown avg `0.1743` n `425`
- 1h: commodity avg `0.059` n `12`; crypto_alt avg `0.1435` n `228`; crypto_major avg `0.0598` n `8`; equity avg `0.2905` n `74`; fx avg `-0.0035` n `6`; index avg `0.0708` n `23`; metal avg `0.008` n `18`; unknown avg `0.0294` n `425`
- 4h: commodity avg `0.1345` n `12`; crypto_alt avg `-0.3588` n `228`; crypto_major avg `-0.6022` n `8`; equity avg `0.1266` n `74`; fx avg `0.0032` n `6`; index avg `0.0538` n `23`; metal avg `-0.0595` n `18`; unknown avg `0.0902` n `425`
- 24h: commodity avg `-1.295` n `12`; crypto_alt avg `-4.4783` n `228`; crypto_major avg `-4.4769` n `8`; equity avg `-6.8217` n `74`; fx avg `-0.2727` n `6`; index avg `-4.1287` n `23`; metal avg `-4.3731` n `18`; unknown avg `0.4555` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
