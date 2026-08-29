# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T02:52:23.778011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.38` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `0.2194` n `231`; crypto_major avg `0.1589` n `8`; equity avg `0.0247` n `127`; fx avg `-0.0018` n `6`; index avg `0.0107` n `26`; metal avg `-0.0087` n `20`; unknown avg `0.0677` n `793`
- 1h: commodity avg `0.0014` n `12`; crypto_alt avg `-0.0711` n `231`; crypto_major avg `-0.148` n `8`; equity avg `0.0491` n `127`; fx avg `-0.0046` n `6`; index avg `0.0269` n `26`; metal avg `0.0054` n `20`; unknown avg `-0.1892` n `793`
- 4h: commodity avg `0.024` n `12`; crypto_alt avg `0.193` n `231`; crypto_major avg `-0.0421` n `8`; equity avg `0.1136` n `127`; fx avg `-0.0033` n `6`; index avg `0.0346` n `26`; metal avg `0.0027` n `20`; unknown avg `-0.3498` n `793`
- 24h: commodity avg `-0.1187` n `12`; crypto_alt avg `-1.4665` n `231`; crypto_major avg `-2.3471` n `8`; equity avg `-1.9427` n `127`; fx avg `-0.1085` n `6`; index avg `-0.1996` n `26`; metal avg `-0.2379` n `20`; unknown avg `-0.3639` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
