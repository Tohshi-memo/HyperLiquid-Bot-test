# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T06:07:28.750342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0247` n `12`; crypto_alt avg `-0.0601` n `230`; crypto_major avg `-0.0359` n `8`; equity avg `0.0029` n `113`; fx avg `0.0153` n `6`; index avg `0.005` n `25`; metal avg `0.0998` n `20`; unknown avg `-0.0669` n `753`
- 1h: commodity avg `0.0256` n `12`; crypto_alt avg `-0.153` n `230`; crypto_major avg `-0.0926` n `8`; equity avg `-0.2085` n `113`; fx avg `0.0222` n `6`; index avg `-0.0406` n `25`; metal avg `-0.1337` n `20`; unknown avg `-0.075` n `753`
- 4h: commodity avg `0.0397` n `12`; crypto_alt avg `-0.4307` n `230`; crypto_major avg `-0.1208` n `8`; equity avg `0.0589` n `113`; fx avg `-0.003` n `6`; index avg `0.0224` n `25`; metal avg `-0.2894` n `20`; unknown avg `-0.0637` n `753`
- 24h: commodity avg `0.9791` n `12`; crypto_alt avg `-1.0346` n `230`; crypto_major avg `-0.8937` n `8`; equity avg `-1.0706` n `113`; fx avg `0.0785` n `6`; index avg `0.0225` n `25`; metal avg `0.1693` n `20`; unknown avg `103.7108` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
