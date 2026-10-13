# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T19:52:31.633458+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `13`; crypto_alt avg `0.0045` n `235`; crypto_major avg `-0.092` n `8`; equity avg `-0.0597` n `151`; fx avg `-0.0016` n `6`; index avg `-0.0106` n `26`; metal avg `-0.0172` n `20`; unknown avg `47.9035` n `1119`
- 1h: commodity avg `0.0841` n `13`; crypto_alt avg `0.1221` n `235`; crypto_major avg `-0.1387` n `8`; equity avg `0.0927` n `151`; fx avg `-0.0073` n `6`; index avg `0.0101` n `26`; metal avg `-0.015` n `20`; unknown avg `29.141` n `1117`
- 4h: commodity avg `0.1583` n `13`; crypto_alt avg `0.8595` n `235`; crypto_major avg `0.1309` n `8`; equity avg `0.6092` n `151`; fx avg `0.0086` n `6`; index avg `0.1017` n `26`; metal avg `-0.0011` n `20`; unknown avg `2.4193` n `1111`
- 24h: commodity avg `0.7274` n `13`; crypto_alt avg `-1.5478` n `235`; crypto_major avg `-0.6291` n `8`; equity avg `-0.9304` n `151`; fx avg `0.1729` n `6`; index avg `-0.1727` n `26`; metal avg `-0.2238` n `20`; unknown avg `1.4299` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1598`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1433`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1183`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0921`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0814`, n `666`, weak_sample_signal
