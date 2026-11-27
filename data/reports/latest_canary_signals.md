# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T15:07:40.302940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `-3.2557` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-3.236` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.1764` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `3.1698` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.0118` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.8478` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0906` n `13`; crypto_alt avg `-0.524` n `239`; crypto_major avg `-0.5443` n `8`; equity avg `-0.0998` n `168`; fx avg `-0.0156` n `6`; index avg `0.0162` n `27`; metal avg `-0.0708` n `20`; unknown avg `1.6231` n `1250`
- 1h: commodity avg `-0.0724` n `13`; crypto_alt avg `-2.651` n `239`; crypto_major avg `-3.3084` n `8`; equity avg `-1.9424` n `168`; fx avg `-0.013` n `6`; index avg `-0.1386` n `27`; metal avg `-0.0527` n `20`; unknown avg `321.8001` n `1258`
- 4h: commodity avg `-0.344` n `13`; crypto_alt avg `-2.4727` n `239`; crypto_major avg `-3.3558` n `8`; equity avg `-2.46` n `168`; fx avg `-0.0305` n `6`; index avg `-0.1794` n `27`; metal avg `-0.508` n `20`; unknown avg `3.7602` n `1249`
- 24h: commodity avg `-0.3625` n `13`; crypto_alt avg `0.4171` n `239`; crypto_major avg `0.5772` n `8`; equity avg `1.5427` n `168`; fx avg `-0.1137` n `6`; index avg `0.1325` n `27`; metal avg `0.6756` n `20`; unknown avg `86.0572` n `1021`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
