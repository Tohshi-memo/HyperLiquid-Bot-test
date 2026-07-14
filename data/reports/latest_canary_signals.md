# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T09:37:34.901342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.026` n `12`; crypto_alt avg `-0.1804` n `230`; crypto_major avg `-0.2392` n `8`; equity avg `-0.0287` n `92`; fx avg `-0.0055` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0268` n `20`; unknown avg `-0.0285` n `766`
- 1h: commodity avg `0.0148` n `12`; crypto_alt avg `-0.2152` n `230`; crypto_major avg `-0.2602` n `8`; equity avg `-0.1083` n `92`; fx avg `0.0167` n `6`; index avg `-0.0342` n `25`; metal avg `-0.0106` n `20`; unknown avg `-0.0029` n `766`
- 4h: commodity avg `0.3131` n `12`; crypto_alt avg `-0.2696` n `230`; crypto_major avg `-0.3114` n `8`; equity avg `0.1412` n `92`; fx avg `0.0658` n `6`; index avg `-0.0327` n `25`; metal avg `-0.1089` n `20`; unknown avg `-0.1089` n `750`
- 24h: commodity avg `1.6108` n `12`; crypto_alt avg `-1.0554` n `230`; crypto_major avg `-0.9674` n `8`; equity avg `-0.6536` n `92`; fx avg `-0.0406` n `6`; index avg `-0.1648` n `25`; metal avg `-0.1829` n `20`; unknown avg `-0.3371` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
