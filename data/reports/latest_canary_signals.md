# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T05:22:29.526930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `13`; crypto_alt avg `0.5021` n `235`; crypto_major avg `0.3676` n `8`; equity avg `0.0388` n `150`; fx avg `-0.0005` n `6`; index avg `0.0074` n `26`; metal avg `-0.0244` n `20`; unknown avg `0.2119` n `1077`
- 1h: commodity avg `0.0167` n `13`; crypto_alt avg `0.8525` n `235`; crypto_major avg `0.6048` n `8`; equity avg `0.2856` n `150`; fx avg `0.012` n `6`; index avg `0.064` n `26`; metal avg `-0.0137` n `20`; unknown avg `0.2004` n `1075`
- 4h: commodity avg `0.1438` n `13`; crypto_alt avg `-0.5287` n `235`; crypto_major avg `-0.6172` n `8`; equity avg `-0.3806` n `150`; fx avg `0.0447` n `6`; index avg `-0.0077` n `26`; metal avg `0.0259` n `20`; unknown avg `-0.3967` n `1069`
- 24h: commodity avg `0.4105` n `13`; crypto_alt avg `-0.6339` n `235`; crypto_major avg `-1.9363` n `8`; equity avg `-1.1634` n `150`; fx avg `-0.1182` n `6`; index avg `-0.1873` n `26`; metal avg `-0.1453` n `20`; unknown avg `246.8129` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
