# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T03:52:33.654029+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.775` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.7081` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.6358` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-3.1652` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `3.1096` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-3.0459` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.6746` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-2.1086` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0047` n `13`; crypto_alt avg `-0.5436` n `239`; crypto_major avg `-0.6507` n `8`; equity avg `-0.0524` n `166`; fx avg `-0.0005` n `6`; index avg `0.0001` n `27`; metal avg `0.0118` n `20`; unknown avg `4.1936` n `1262`
- 1h: commodity avg `-0.0579` n `13`; crypto_alt avg `-2.9465` n `239`; crypto_major avg `-3.2231` n `8`; equity avg `-1.1145` n `166`; fx avg `-0.0179` n `6`; index avg `-0.1135` n `27`; metal avg `-0.1772` n `20`; unknown avg `33.9991` n `1256`
- 4h: commodity avg `-0.0431` n `13`; crypto_alt avg `-3.5285` n `239`; crypto_major avg `-3.8181` n `8`; equity avg `-1.1435` n `166`; fx avg `-0.0153` n `6`; index avg `-0.11` n `27`; metal avg `-0.1823` n `20`; unknown avg `161.4267` n `1250`
- 24h: commodity avg `0.2014` n `13`; crypto_alt avg `-7.0183` n `239`; crypto_major avg `-8.9886` n `8`; equity avg `-6.3863` n `166`; fx avg `-0.0646` n `6`; index avg `-0.67` n `27`; metal avg `-0.3257` n `20`; unknown avg `12.1034` n `1119`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
