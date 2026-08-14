# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T01:07:26.821413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0722` n `12`; crypto_alt avg `-0.0191` n `230`; crypto_major avg `0.0102` n `8`; equity avg `-0.1396` n `113`; fx avg `0.0051` n `6`; index avg `-0.0354` n `25`; metal avg `-0.0568` n `20`; unknown avg `-0.0353` n `787`
- 1h: commodity avg `0.0333` n `12`; crypto_alt avg `-0.0399` n `230`; crypto_major avg `0.0277` n `8`; equity avg `-0.3254` n `113`; fx avg `-0.0121` n `6`; index avg `-0.097` n `25`; metal avg `-0.1992` n `20`; unknown avg `0.5637` n `787`
- 4h: commodity avg `0.0827` n `12`; crypto_alt avg `0.2681` n `230`; crypto_major avg `0.0105` n `8`; equity avg `-0.1363` n `113`; fx avg `-0.0133` n `6`; index avg `-0.0459` n `25`; metal avg `-0.1797` n `20`; unknown avg `0.7826` n `787`
- 24h: commodity avg `-0.2313` n `12`; crypto_alt avg `0.3145` n `230`; crypto_major avg `0.5452` n `8`; equity avg `1.0713` n `113`; fx avg `0.054` n `6`; index avg `0.2266` n `25`; metal avg `-0.8008` n `20`; unknown avg `1.1524` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2432`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1861`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
