# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T22:52:23.797669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0346` n `12`; crypto_alt avg `0.1268` n `228`; crypto_major avg `0.0904` n `8`; equity avg `0.0155` n `69`; fx avg `-0.0022` n `6`; index avg `-0.088` n `23`; metal avg `0.0951` n `18`; unknown avg `0.9285` n `421`
- 1h: commodity avg `0.4126` n `12`; crypto_alt avg `0.4723` n `228`; crypto_major avg `0.3953` n `8`; equity avg `0.0126` n `69`; fx avg `0.0034` n `6`; index avg `-0.0883` n `23`; metal avg `0.0567` n `18`; unknown avg `1.6798` n `421`
- 4h: commodity avg `0.2405` n `12`; crypto_alt avg `1.8084` n `228`; crypto_major avg `1.2905` n `8`; equity avg `0.0362` n `69`; fx avg `-0.017` n `6`; index avg `0.1568` n `23`; metal avg `0.0742` n `18`; unknown avg `1.7233` n `421`
- 24h: commodity avg `0.8278` n `12`; crypto_alt avg `1.2869` n `228`; crypto_major avg `0.8676` n `8`; equity avg `0.7675` n `69`; fx avg `-0.0382` n `6`; index avg `0.2256` n `23`; metal avg `-0.0448` n `18`; unknown avg `2.2769` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3292`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2359`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
