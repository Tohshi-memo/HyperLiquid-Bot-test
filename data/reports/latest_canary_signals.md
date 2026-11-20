# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T17:07:37.762608+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.823` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.443` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.365` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0001` n `13`; crypto_alt avg `-0.6779` n `239`; crypto_major avg `-0.659` n `8`; equity avg `-0.4999` n `166`; fx avg `0.011` n `6`; index avg `-0.0309` n `27`; metal avg `-0.0382` n `20`; unknown avg `1.1162` n `1251`
- 1h: commodity avg `0.0704` n `13`; crypto_alt avg `-0.6471` n `239`; crypto_major avg `-0.7239` n `8`; equity avg `-1.5735` n `166`; fx avg `0.0243` n `6`; index avg `-0.1496` n `27`; metal avg `-0.1376` n `20`; unknown avg `159.0877` n `1255`
- 4h: commodity avg `0.0872` n `13`; crypto_alt avg `-3.5463` n `239`; crypto_major avg `-3.7358` n `8`; equity avg `-3.3635` n `166`; fx avg `0.0063` n `6`; index avg `-0.2928` n `27`; metal avg `-0.3708` n `20`; unknown avg `160.9584` n `1245`
- 24h: commodity avg `-0.1967` n `13`; crypto_alt avg `-5.7886` n `239`; crypto_major avg `-5.8448` n `8`; equity avg `-8.2028` n `166`; fx avg `0.0346` n `6`; index avg `-0.6653` n `27`; metal avg `-1.092` n `20`; unknown avg `31.6617` n `1151`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
