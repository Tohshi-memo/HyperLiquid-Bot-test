# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T19:07:56.352705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `0.0434` n `230`; crypto_major avg `-0.0482` n `8`; equity avg `0.1376` n `107`; fx avg `0.0159` n `6`; index avg `0.0181` n `25`; metal avg `0.0062` n `20`; unknown avg `-0.0439` n `782`
- 1h: commodity avg `0.023` n `12`; crypto_alt avg `0.142` n `230`; crypto_major avg `-0.0018` n `8`; equity avg `0.1992` n `107`; fx avg `0.0467` n `6`; index avg `0.0422` n `25`; metal avg `-0.0539` n `20`; unknown avg `-0.0304` n `782`
- 4h: commodity avg `-0.237` n `12`; crypto_alt avg `0.4264` n `230`; crypto_major avg `0.0938` n `8`; equity avg `1.0514` n `107`; fx avg `0.0704` n `6`; index avg `0.294` n `25`; metal avg `0.0187` n `20`; unknown avg `-0.2361` n `782`
- 24h: commodity avg `-1.2177` n `12`; crypto_alt avg `-0.1105` n `230`; crypto_major avg `0.3884` n `8`; equity avg `4.174` n `107`; fx avg `0.162` n `6`; index avg `0.8496` n `25`; metal avg `1.0051` n `20`; unknown avg `0.4651` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
