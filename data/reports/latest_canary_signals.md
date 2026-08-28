# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T19:22:25.033260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6523` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.4153` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8922` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0234` n `12`; crypto_alt avg `0.2548` n `231`; crypto_major avg `0.1485` n `8`; equity avg `0.0497` n `127`; fx avg `0.0012` n `6`; index avg `0.0162` n `26`; metal avg `-0.0096` n `20`; unknown avg `-0.0922` n `793`
- 1h: commodity avg `-0.0313` n `12`; crypto_alt avg `0.3683` n `231`; crypto_major avg `0.085` n `8`; equity avg `-0.1327` n `127`; fx avg `-0.0046` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0499` n `20`; unknown avg `0.8639` n `793`
- 4h: commodity avg `-0.0024` n `12`; crypto_alt avg `-2.424` n `231`; crypto_major avg `-2.6547` n `8`; equity avg `-1.3715` n `127`; fx avg `-0.0205` n `6`; index avg `-0.2394` n `26`; metal avg `-0.7625` n `20`; unknown avg `1.2134` n `793`
- 24h: commodity avg `-0.2468` n `12`; crypto_alt avg `-3.3874` n `231`; crypto_major avg `-3.8645` n `8`; equity avg `-2.2291` n `127`; fx avg `-0.1161` n `6`; index avg `-0.1283` n `26`; metal avg `-0.3863` n `20`; unknown avg `-0.6588` n `760`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
