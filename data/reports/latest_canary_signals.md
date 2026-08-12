# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T04:22:29.159587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0229` n `12`; crypto_alt avg `0.0875` n `230`; crypto_major avg `0.1666` n `8`; equity avg `-0.0317` n `113`; fx avg `-0.0017` n `6`; index avg `0.0087` n `25`; metal avg `-0.015` n `20`; unknown avg `1.3785` n `786`
- 1h: commodity avg `0.0266` n `12`; crypto_alt avg `0.0195` n `230`; crypto_major avg `0.1629` n `8`; equity avg `0.0216` n `113`; fx avg `-0.0286` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0417` n `20`; unknown avg `0.7541` n `786`
- 4h: commodity avg `0.1162` n `12`; crypto_alt avg `0.3393` n `230`; crypto_major avg `0.3014` n `8`; equity avg `0.665` n `113`; fx avg `0.0167` n `6`; index avg `0.1507` n `25`; metal avg `0.1331` n `20`; unknown avg `0.2588` n `786`
- 24h: commodity avg `0.3499` n `12`; crypto_alt avg `-0.9605` n `230`; crypto_major avg `0.7078` n `8`; equity avg `1.6389` n `113`; fx avg `0.0326` n `6`; index avg `0.138` n `25`; metal avg `-0.1394` n `20`; unknown avg `-0.117` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2252`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2248`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2166`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.207`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.2058`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
