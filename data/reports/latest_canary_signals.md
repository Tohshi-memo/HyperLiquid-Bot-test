# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T03:29:25.649906+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1718` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9805` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8976` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.003` n `13`; crypto_alt avg `-0.4875` n `238`; crypto_major avg `-0.333` n `8`; equity avg `-0.2414` n `155`; fx avg `0.0094` n `6`; index avg `-0.0654` n `27`; metal avg `-0.0646` n `20`; unknown avg `1.394` n `1230`
- 1h: commodity avg `-0.0104` n `13`; crypto_alt avg `-0.6727` n `238`; crypto_major avg `-0.3163` n `8`; equity avg `-0.1951` n `155`; fx avg `-0.0034` n `6`; index avg `-0.0376` n `27`; metal avg `-0.1694` n `20`; unknown avg `3.0705` n `1216`
- 4h: commodity avg `-0.0257` n `13`; crypto_alt avg `-2.9364` n `238`; crypto_major avg `-2.1975` n `8`; equity avg `-1.3508` n `155`; fx avg `-0.105` n `6`; index avg `-0.217` n `27`; metal avg `-0.2999` n `20`; unknown avg `3.6278` n `1196`
- 24h: commodity avg `-0.0515` n `13`; crypto_alt avg `-2.8232` n `238`; crypto_major avg `-2.0055` n `8`; equity avg `-1.5688` n `154`; fx avg `-0.0018` n `6`; index avg `-0.2136` n `27`; metal avg `-0.3124` n `20`; unknown avg `29.2924` n `982`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
