# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T14:29:03.949363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.57` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.7161` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6761` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1131` n `13`; crypto_alt avg `-0.4424` n `238`; crypto_major avg `-0.3575` n `8`; equity avg `0.0362` n `155`; fx avg `-0.0044` n `6`; index avg `-0.0123` n `27`; metal avg `-0.0522` n `20`; unknown avg `0.3486` n `1194`
- 1h: commodity avg `0.1389` n `13`; crypto_alt avg `-0.6025` n `238`; crypto_major avg `-0.4964` n `8`; equity avg `-0.0722` n `155`; fx avg `0.0387` n `6`; index avg `-0.0044` n `27`; metal avg `-0.1238` n `20`; unknown avg `1.3617` n `1154`
- 4h: commodity avg `0.233` n `13`; crypto_alt avg `-1.6876` n `238`; crypto_major avg `-1.6901` n `8`; equity avg `-0.6515` n `155`; fx avg `0.0787` n `6`; index avg `0.026` n `27`; metal avg `-0.014` n `20`; unknown avg `2.3212` n `1150`
- 24h: commodity avg `0.4355` n `13`; crypto_alt avg `0.3973` n `238`; crypto_major avg `0.5887` n `8`; equity avg `2.0453` n `154`; fx avg `0.1442` n `6`; index avg `0.4327` n `27`; metal avg `-0.0227` n `20`; unknown avg `8.6019` n `1066`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1611`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
