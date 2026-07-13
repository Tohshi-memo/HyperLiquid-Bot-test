# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T12:52:29.827511+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0882` n `12`; crypto_alt avg `0.1247` n `230`; crypto_major avg `0.051` n `8`; equity avg `0.1855` n `92`; fx avg `-0.0147` n `6`; index avg `0.0499` n `25`; metal avg `0.086` n `20`; unknown avg `-0.0266` n `766`
- 1h: commodity avg `0.0446` n `12`; crypto_alt avg `-0.2999` n `230`; crypto_major avg `-0.538` n `8`; equity avg `-0.2104` n `92`; fx avg `-0.0008` n `6`; index avg `-0.0313` n `25`; metal avg `0.0131` n `20`; unknown avg `0.0584` n `766`
- 4h: commodity avg `0.2236` n `12`; crypto_alt avg `-0.4108` n `230`; crypto_major avg `-0.9207` n `8`; equity avg `-0.1014` n `92`; fx avg `-0.0282` n `6`; index avg `-0.0487` n `25`; metal avg `-0.0626` n `20`; unknown avg `0.0377` n `766`
- 24h: commodity avg `-0.0101` n `12`; crypto_alt avg `-1.3696` n `230`; crypto_major avg `-1.9377` n `8`; equity avg `-2.1562` n `92`; fx avg `-0.0535` n `6`; index avg `-0.4439` n `25`; metal avg `-0.1955` n `20`; unknown avg `-0.1819` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
