# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T05:37:24.350744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1542` n `12`; crypto_alt avg `0.0079` n `230`; crypto_major avg `-0.0538` n `8`; equity avg `0.139` n `92`; fx avg `0.0153` n `6`; index avg `0.0275` n `25`; metal avg `0.0901` n `20`; unknown avg `0.0246` n `766`
- 1h: commodity avg `-0.1524` n `12`; crypto_alt avg `0.1991` n `230`; crypto_major avg `0.1566` n `8`; equity avg `0.7732` n `92`; fx avg `0.0461` n `6`; index avg `0.1744` n `25`; metal avg `0.1394` n `20`; unknown avg `0.5559` n `766`
- 4h: commodity avg `-0.1235` n `12`; crypto_alt avg `0.1838` n `230`; crypto_major avg `0.3242` n `8`; equity avg `0.4994` n `92`; fx avg `0.012` n `6`; index avg `0.1231` n `25`; metal avg `0.454` n `20`; unknown avg `-0.0461` n `766`
- 24h: commodity avg `0.7892` n `12`; crypto_alt avg `-0.3962` n `230`; crypto_major avg `-0.5289` n `8`; equity avg `-0.3998` n `92`; fx avg `-0.1637` n `6`; index avg `-0.0044` n `25`; metal avg `0.1495` n `20`; unknown avg `-0.2205` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
