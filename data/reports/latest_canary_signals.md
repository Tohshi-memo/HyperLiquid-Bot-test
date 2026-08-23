# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T01:37:26.254909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `12`; crypto_alt avg `-0.2907` n `230`; crypto_major avg `-0.2504` n `8`; equity avg `-0.0017` n `121`; fx avg `-0.0048` n `6`; index avg `-0.0053` n `25`; metal avg `-0.003` n `20`; unknown avg `-0.0177` n `794`
- 1h: commodity avg `-0.0304` n `12`; crypto_alt avg `-0.3941` n `230`; crypto_major avg `0.0617` n `8`; equity avg `0.0173` n `121`; fx avg `-0.0122` n `6`; index avg `0.0017` n `25`; metal avg `0.0137` n `20`; unknown avg `-0.0243` n `794`
- 4h: commodity avg `-0.0326` n `12`; crypto_alt avg `0.8882` n `230`; crypto_major avg `1.3731` n `8`; equity avg `0.2162` n `121`; fx avg `0.0308` n `6`; index avg `0.0238` n `25`; metal avg `0.0003` n `20`; unknown avg `0.7876` n `794`
- 24h: commodity avg `0.0739` n `12`; crypto_alt avg `-2.9085` n `230`; crypto_major avg `0.4995` n `8`; equity avg `-0.2172` n `121`; fx avg `0.1013` n `6`; index avg `-0.0461` n `25`; metal avg `-0.0268` n `20`; unknown avg `2.7286` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
