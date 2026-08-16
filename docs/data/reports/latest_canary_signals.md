# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T06:07:29.783012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `0.0391` n `230`; crypto_major avg `0.0046` n `8`; equity avg `0.0089` n `114`; fx avg `-0.0013` n `6`; index avg `0.0025` n `25`; metal avg `-0.0049` n `20`; unknown avg `-0.0027` n `759`
- 1h: commodity avg `0.0041` n `12`; crypto_alt avg `0.0399` n `230`; crypto_major avg `-0.0789` n `8`; equity avg `0.0933` n `114`; fx avg `-0.0012` n `6`; index avg `0.0077` n `25`; metal avg `0.0137` n `20`; unknown avg `-0.0145` n `759`
- 4h: commodity avg `-0.0321` n `12`; crypto_alt avg `0.1415` n `230`; crypto_major avg `0.0028` n `8`; equity avg `0.1989` n `114`; fx avg `-0.0002` n `6`; index avg `0.016` n `25`; metal avg `0.0259` n `20`; unknown avg `-0.0016` n `759`
- 24h: commodity avg `-0.0984` n `12`; crypto_alt avg `-0.2313` n `230`; crypto_major avg `-0.0741` n `8`; equity avg `0.3996` n `114`; fx avg `-0.0261` n `6`; index avg `0.0533` n `25`; metal avg `0.0372` n `20`; unknown avg `0.013` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2177`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1841`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
