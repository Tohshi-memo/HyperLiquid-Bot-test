# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T14:52:35.941801+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.6` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.5032` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0008` n `13`; crypto_alt avg `0.2931` n `238`; crypto_major avg `0.2003` n `8`; equity avg `-0.0022` n `155`; fx avg `0.0076` n `6`; index avg `0.0005` n `27`; metal avg `-0.0134` n `20`; unknown avg `1.7165` n `1238`
- 1h: commodity avg `0.0058` n `13`; crypto_alt avg `0.0973` n `238`; crypto_major avg `0.086` n `8`; equity avg `0.0908` n `155`; fx avg `0.0217` n `6`; index avg `0.0238` n `27`; metal avg `-0.0931` n `20`; unknown avg `1.836` n `1168`
- 4h: commodity avg `0.1639` n `13`; crypto_alt avg `-1.3335` n `238`; crypto_major avg `-1.5208` n `8`; equity avg `-1.0028` n `155`; fx avg `0.1168` n `6`; index avg `-0.0176` n `27`; metal avg `-0.0392` n `20`; unknown avg `1.5821` n `1150`
- 24h: commodity avg `0.5466` n `13`; crypto_alt avg `0.3688` n `238`; crypto_major avg `0.4198` n `8`; equity avg `1.3407` n `154`; fx avg `0.1941` n `6`; index avg `0.3168` n `27`; metal avg `-0.1457` n `20`; unknown avg `8.8836` n `1066`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
