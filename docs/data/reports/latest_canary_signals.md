# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T12:52:25.319568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0547` n `13`; crypto_alt avg `0.177` n `235`; crypto_major avg `0.2134` n `8`; equity avg `0.0956` n `151`; fx avg `0.0118` n `6`; index avg `0.0085` n `26`; metal avg `0.036` n `20`; unknown avg `0.5676` n `1134`
- 1h: commodity avg `0.0492` n `13`; crypto_alt avg `-0.2323` n `235`; crypto_major avg `-0.4395` n `8`; equity avg `-0.0326` n `151`; fx avg `0.0096` n `6`; index avg `-0.0084` n `26`; metal avg `-0.0641` n `20`; unknown avg `-0.0221` n `1126`
- 4h: commodity avg `0.2999` n `13`; crypto_alt avg `-1.1471` n `235`; crypto_major avg `-0.9578` n `8`; equity avg `-0.1659` n `151`; fx avg `0.0095` n `6`; index avg `-0.0513` n `26`; metal avg `0.0129` n `20`; unknown avg `0.116` n `1033`
- 24h: commodity avg `0.1562` n `13`; crypto_alt avg `0.7271` n `235`; crypto_major avg `0.3637` n `8`; equity avg `-1.4088` n `151`; fx avg `-0.129` n `6`; index avg `-0.1732` n `26`; metal avg `-0.0378` n `20`; unknown avg `0.8679` n `862`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2433`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
