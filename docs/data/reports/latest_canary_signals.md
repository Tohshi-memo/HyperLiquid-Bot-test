# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T03:52:14.510448+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0355` n `12`; crypto_alt avg `-0.0744` n `228`; crypto_major avg `0.0124` n `8`; equity avg `0.0923` n `66`; fx avg `0.0104` n `5`; index avg `0.0073` n `23`; metal avg `0.1782` n `18`; unknown avg `-0.1047` n `383`
- 1h: commodity avg `0.0021` n `12`; crypto_alt avg `-0.1638` n `228`; crypto_major avg `-0.0097` n `8`; equity avg `0.0121` n `66`; fx avg `0.0106` n `5`; index avg `0.1482` n `23`; metal avg `0.0223` n `18`; unknown avg `0.1655` n `383`
- 4h: commodity avg `0.6289` n `12`; crypto_alt avg `0.4777` n `228`; crypto_major avg `-0.3217` n `8`; equity avg `-0.2685` n `66`; fx avg `0.0735` n `5`; index avg `-0.0655` n `23`; metal avg `-0.9313` n `18`; unknown avg `-0.8348` n `383`
- 24h: commodity avg `2.6735` n `12`; crypto_alt avg `-11.0255` n `228`; crypto_major avg `-3.465` n `8`; equity avg `-3.0566` n `65`; fx avg `-0.0693` n `5`; index avg `-1.7742` n `23`; metal avg `-6.2925` n `18`; unknown avg `550.1112` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
