# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T13:52:29.124723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.51` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.5581` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5279` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0268` n `13`; crypto_alt avg `-0.5256` n `238`; crypto_major avg `-0.5534` n `8`; equity avg `-0.2332` n `155`; fx avg `0.0122` n `6`; index avg `-0.0614` n `27`; metal avg `-0.0202` n `20`; unknown avg `0.3795` n `1224`
- 1h: commodity avg `0.0618` n `13`; crypto_alt avg `-0.3227` n `238`; crypto_major avg `-0.5291` n `8`; equity avg `-0.6011` n `155`; fx avg `0.0399` n `6`; index avg `-0.0236` n `27`; metal avg `-0.0905` n `20`; unknown avg `1.2504` n `1220`
- 4h: commodity avg `0.2802` n `13`; crypto_alt avg `-1.4504` n `238`; crypto_major avg `-1.5348` n `8`; equity avg `-0.7115` n `155`; fx avg `0.0785` n `6`; index avg `-0.0069` n `27`; metal avg `0.0233` n `20`; unknown avg `1.0471` n `1214`
- 24h: commodity avg `0.3621` n `13`; crypto_alt avg `0.7164` n `238`; crypto_major avg `0.6732` n `8`; equity avg `1.9469` n `154`; fx avg `0.159` n `6`; index avg `0.4146` n `27`; metal avg `0.1914` n `20`; unknown avg `3.1126` n `1058`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
