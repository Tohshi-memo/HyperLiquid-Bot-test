# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T05:07:28.856980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `-0.1284` n `230`; crypto_major avg `-0.2096` n `8`; equity avg `-0.3159` n `96`; fx avg `-0.0016` n `6`; index avg `-0.0327` n `25`; metal avg `-0.0482` n `20`; unknown avg `-0.2237` n `768`
- 1h: commodity avg `0.0273` n `12`; crypto_alt avg `-0.0087` n `230`; crypto_major avg `-0.1392` n `8`; equity avg `-0.4018` n `96`; fx avg `-0.0173` n `6`; index avg `-0.1007` n `25`; metal avg `-0.0812` n `20`; unknown avg `-0.2463` n `768`
- 4h: commodity avg `-0.0942` n `12`; crypto_alt avg `-0.4543` n `230`; crypto_major avg `-0.9139` n `8`; equity avg `-1.6626` n `94`; fx avg `0.0006` n `6`; index avg `-0.2805` n `25`; metal avg `-0.2727` n `20`; unknown avg `0.3446` n `768`
- 24h: commodity avg `-0.0366` n `12`; crypto_alt avg `-1.9768` n `230`; crypto_major avg `-3.065` n `8`; equity avg `-5.7061` n `94`; fx avg `-0.1276` n `6`; index avg `-0.7983` n `25`; metal avg `-0.891` n `20`; unknown avg `-0.496` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
