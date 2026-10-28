# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T13:07:34.321563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.44` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.06` n `13`; crypto_alt avg `0.1478` n `238`; crypto_major avg `-0.0576` n `8`; equity avg `0.0153` n `154`; fx avg `0.004` n `6`; index avg `0.0344` n `27`; metal avg `-0.0004` n `20`; unknown avg `0.9823` n `1233`
- 1h: commodity avg `0.0823` n `13`; crypto_alt avg `-0.5721` n `238`; crypto_major avg `-0.5945` n `8`; equity avg `-0.1306` n `154`; fx avg `-0.0195` n `6`; index avg `0.0376` n `27`; metal avg `0.0934` n `20`; unknown avg `1.7449` n `1231`
- 4h: commodity avg `0.1545` n `13`; crypto_alt avg `-0.693` n `238`; crypto_major avg `-0.8234` n `8`; equity avg `-0.0868` n `154`; fx avg `0.054` n `6`; index avg `0.0612` n `27`; metal avg `0.0793` n `20`; unknown avg `1.3335` n `1196`
- 24h: commodity avg `0.1601` n `13`; crypto_alt avg `1.0174` n `238`; crypto_major avg `1.0363` n `8`; equity avg `2.5583` n `154`; fx avg `0.1043` n `6`; index avg `0.4161` n `27`; metal avg `0.2798` n `20`; unknown avg `6.5873` n `1068`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
