# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T13:37:25.071364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1102` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.1804` n `12`; crypto_alt avg `0.1599` n `230`; crypto_major avg `0.0967` n `8`; equity avg `0.3995` n `107`; fx avg `-0.0163` n `6`; index avg `0.0361` n `25`; metal avg `0.0544` n `20`; unknown avg `-0.0017` n `781`
- 1h: commodity avg `-0.4761` n `12`; crypto_alt avg `-0.0166` n `230`; crypto_major avg `-0.0238` n `8`; equity avg `0.5364` n `107`; fx avg `-0.0401` n `6`; index avg `0.1116` n `25`; metal avg `-0.0581` n `20`; unknown avg `0.0524` n `781`
- 4h: commodity avg `-1.3844` n `12`; crypto_alt avg `0.1385` n `230`; crypto_major avg `0.7258` n `8`; equity avg `1.5071` n `107`; fx avg `-0.1217` n `6`; index avg `0.2688` n `25`; metal avg `0.5801` n `20`; unknown avg `0.1072` n `781`
- 24h: commodity avg `-0.874` n `12`; crypto_alt avg `0.6102` n `230`; crypto_major avg `1.489` n `8`; equity avg `5.4913` n `107`; fx avg `0.0509` n `6`; index avg `0.7152` n `25`; metal avg `1.1889` n `20`; unknown avg `0.8353` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
