# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T17:37:28.151537+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0238` n `13`; crypto_alt avg `-0.0956` n `235`; crypto_major avg `-0.0889` n `8`; equity avg `0.0504` n `151`; fx avg `0.0108` n `6`; index avg `0.0001` n `26`; metal avg `0.0031` n `20`; unknown avg `-0.0299` n `1135`
- 1h: commodity avg `0.0404` n `13`; crypto_alt avg `-0.174` n `235`; crypto_major avg `-0.2228` n `8`; equity avg `-0.2732` n `151`; fx avg `0.0155` n `6`; index avg `-0.0303` n `26`; metal avg `-0.0016` n `20`; unknown avg `-0.4026` n `1133`
- 4h: commodity avg `0.5754` n `13`; crypto_alt avg `-0.3878` n `235`; crypto_major avg `-0.2425` n `8`; equity avg `0.4874` n `151`; fx avg `-0.0052` n `6`; index avg `0.0172` n `26`; metal avg `-0.2733` n `20`; unknown avg `0.4657` n `1099`
- 24h: commodity avg `0.5117` n `13`; crypto_alt avg `-1.4154` n `235`; crypto_major avg `-0.2186` n `8`; equity avg `-0.9862` n `151`; fx avg `0.1538` n `6`; index avg `-0.1959` n `26`; metal avg `-0.2546` n `20`; unknown avg `0.2139` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1627`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1476`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1222`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0905`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0904`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
