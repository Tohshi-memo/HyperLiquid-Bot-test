# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T04:22:27.837723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0471` n `12`; crypto_alt avg `0.3087` n `230`; crypto_major avg `0.2492` n `8`; equity avg `0.0795` n `108`; fx avg `-0.0192` n `6`; index avg `-0.0104` n `25`; metal avg `-0.0229` n `20`; unknown avg `0.0774` n `782`
- 1h: commodity avg `-0.1787` n `12`; crypto_alt avg `0.2523` n `230`; crypto_major avg `0.2621` n `8`; equity avg `0.0485` n `108`; fx avg `-0.0072` n `6`; index avg `-0.0222` n `25`; metal avg `-0.0042` n `20`; unknown avg `0.0884` n `782`
- 4h: commodity avg `0.0057` n `12`; crypto_alt avg `-0.1152` n `230`; crypto_major avg `-0.5026` n `8`; equity avg `-0.0173` n `108`; fx avg `-0.0571` n `6`; index avg `-0.1134` n `25`; metal avg `-0.0726` n `20`; unknown avg `-0.1687` n `782`
- 24h: commodity avg `-0.1089` n `12`; crypto_alt avg `0.2214` n `230`; crypto_major avg `0.1956` n `8`; equity avg `-1.7372` n `108`; fx avg `0.0013` n `6`; index avg `-0.3341` n `25`; metal avg `0.4732` n `20`; unknown avg `0.9544` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1812`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
