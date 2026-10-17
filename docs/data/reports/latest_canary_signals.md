# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T13:07:32.800184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `13`; crypto_alt avg `-0.0229` n `236`; crypto_major avg `0.0167` n `8`; equity avg `0.0175` n `151`; fx avg `0.0018` n `6`; index avg `-0.0024` n `26`; metal avg `-0.0066` n `20`; unknown avg `-0.0295` n `1191`
- 1h: commodity avg `-0.0319` n `13`; crypto_alt avg `-0.6191` n `236`; crypto_major avg `-0.2632` n `8`; equity avg `-0.0763` n `151`; fx avg `0.0021` n `6`; index avg `-0.0141` n `26`; metal avg `-0.0186` n `20`; unknown avg `2.9894` n `1191`
- 4h: commodity avg `-0.0003` n `13`; crypto_alt avg `-1.1963` n `236`; crypto_major avg `-0.6689` n `8`; equity avg `-0.1478` n `151`; fx avg `0.0267` n `6`; index avg `-0.0132` n `26`; metal avg `-0.0233` n `20`; unknown avg `3.171` n `1183`
- 24h: commodity avg `0.4948` n `13`; crypto_alt avg `-2.888` n `236`; crypto_major avg `-1.6005` n `8`; equity avg `-3.2144` n `151`; fx avg `0.0311` n `6`; index avg `-0.5591` n `26`; metal avg `-0.1513` n `20`; unknown avg `10.4936` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1759`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1474`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1183`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1177`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0669`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0634`, n `666`, weak_sample_signal
