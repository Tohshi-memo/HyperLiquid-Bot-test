# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T05:22:30.574894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `0.1228` n `230`; crypto_major avg `0.0903` n `8`; equity avg `0.2326` n `92`; fx avg `0.018` n `6`; index avg `0.0287` n `25`; metal avg `0.0145` n `20`; unknown avg `4.29` n `766`
- 1h: commodity avg `0.0424` n `12`; crypto_alt avg `0.2965` n `230`; crypto_major avg `0.3648` n `8`; equity avg `0.8828` n `92`; fx avg `0.0329` n `6`; index avg `0.2347` n `25`; metal avg `0.1097` n `20`; unknown avg `0.4883` n `766`
- 4h: commodity avg `0.0676` n `12`; crypto_alt avg `0.0195` n `230`; crypto_major avg `0.1758` n `8`; equity avg `0.1367` n `92`; fx avg `0.012` n `6`; index avg `0.047` n `25`; metal avg `0.3104` n `20`; unknown avg `-0.0303` n `766`
- 24h: commodity avg `0.9924` n `12`; crypto_alt avg `-0.367` n `230`; crypto_major avg `-0.4007` n `8`; equity avg `-0.4003` n `92`; fx avg `-0.1771` n `6`; index avg `-0.0046` n `25`; metal avg `0.0731` n `20`; unknown avg `-0.2267` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
