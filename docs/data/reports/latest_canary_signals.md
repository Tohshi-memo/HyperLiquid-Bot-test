# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T18:52:27.748245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0593` n `12`; crypto_alt avg `0.1823` n `230`; crypto_major avg `0.2191` n `8`; equity avg `0.107` n `92`; fx avg `-0.0029` n `6`; index avg `0.0111` n `25`; metal avg `0.0252` n `20`; unknown avg `0.1396` n `766`
- 1h: commodity avg `0.0689` n `12`; crypto_alt avg `0.0915` n `230`; crypto_major avg `0.1591` n `8`; equity avg `0.1652` n `92`; fx avg `-0.0045` n `6`; index avg `0.0226` n `25`; metal avg `0.08` n `20`; unknown avg `0.0494` n `766`
- 4h: commodity avg `0.738` n `12`; crypto_alt avg `-1.1571` n `230`; crypto_major avg `-0.8257` n `8`; equity avg `-0.941` n `92`; fx avg `-0.0137` n `6`; index avg `-0.1608` n `25`; metal avg `-0.1203` n `20`; unknown avg `-0.1795` n `766`
- 24h: commodity avg `0.5443` n `12`; crypto_alt avg `-2.2687` n `230`; crypto_major avg `-3.1175` n `8`; equity avg `-3.1692` n `92`; fx avg `-0.0712` n `6`; index avg `-0.5963` n `25`; metal avg `-0.5201` n `20`; unknown avg `-0.2766` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.19`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1768`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
