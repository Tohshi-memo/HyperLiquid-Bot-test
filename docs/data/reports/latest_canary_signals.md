# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T09:52:36.962227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0446` n `13`; crypto_alt avg `-0.3469` n `239`; crypto_major avg `-0.3201` n `8`; equity avg `-0.3915` n `168`; fx avg `-0.0215` n `6`; index avg `-0.0538` n `27`; metal avg `-0.0465` n `20`; unknown avg `212.2249` n `1265`
- 1h: commodity avg `0.2122` n `13`; crypto_alt avg `-0.7909` n `239`; crypto_major avg `-0.9461` n `8`; equity avg `-1.2585` n `168`; fx avg `-0.0393` n `6`; index avg `-0.1537` n `27`; metal avg `-0.0992` n `20`; unknown avg `0.2144` n `1255`
- 4h: commodity avg `0.1803` n `13`; crypto_alt avg `-0.6787` n `239`; crypto_major avg `-1.1514` n `8`; equity avg `-1.656` n `168`; fx avg `-0.0352` n `6`; index avg `-0.1749` n `27`; metal avg `0.0086` n `20`; unknown avg `190.6147` n `1207`
- 24h: commodity avg `0.4345` n `13`; crypto_alt avg `-2.3718` n `239`; crypto_major avg `-3.2739` n `8`; equity avg `-5.3957` n `167`; fx avg `0.0098` n `6`; index avg `-0.505` n `27`; metal avg `-0.9362` n `20`; unknown avg `709.4655` n `1035`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
