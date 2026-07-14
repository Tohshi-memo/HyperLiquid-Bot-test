# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T02:52:23.694911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0961` n `12`; crypto_alt avg `0.1096` n `230`; crypto_major avg `0.1794` n `8`; equity avg `0.0758` n `92`; fx avg `-0.0221` n `6`; index avg `0.0613` n `25`; metal avg `-0.0101` n `20`; unknown avg `-0.052` n `766`
- 1h: commodity avg `0.0473` n `12`; crypto_alt avg `-0.2807` n `230`; crypto_major avg `-0.0586` n `8`; equity avg `-0.5612` n `92`; fx avg `-0.0076` n `6`; index avg `-0.1507` n `25`; metal avg `0.0843` n `20`; unknown avg `-0.0922` n `766`
- 4h: commodity avg `0.0933` n `12`; crypto_alt avg `0.4815` n `230`; crypto_major avg `0.6435` n `8`; equity avg `-0.4121` n `92`; fx avg `-0.0229` n `6`; index avg `-0.101` n `25`; metal avg `0.0323` n `20`; unknown avg `0.37` n `766`
- 24h: commodity avg `0.9369` n `12`; crypto_alt avg `-1.3296` n `230`; crypto_major avg `-1.7647` n `8`; equity avg `-2.2385` n `92`; fx avg `-0.1521` n `6`; index avg `-0.4361` n `25`; metal avg `-0.2285` n `20`; unknown avg `-0.4258` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1982`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
