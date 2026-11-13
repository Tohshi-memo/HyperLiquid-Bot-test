# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T05:37:27.494485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.094` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.0787` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.934` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0229` n `13`; crypto_alt avg `-0.3921` n `239`; crypto_major avg `-0.5116` n `8`; equity avg `-0.0951` n `162`; fx avg `0.0062` n `6`; index avg `-0.0031` n `27`; metal avg `-0.0069` n `20`; unknown avg `0.2405` n `1258`
- 1h: commodity avg `-0.08` n `13`; crypto_alt avg `0.0596` n `239`; crypto_major avg `0.0229` n `8`; equity avg `-0.3186` n `162`; fx avg `0.0128` n `6`; index avg `-0.0489` n `27`; metal avg `0.0101` n `20`; unknown avg `0.7762` n `1254`
- 4h: commodity avg `-0.05` n `13`; crypto_alt avg `-2.7034` n `239`; crypto_major avg `-3.144` n `8`; equity avg `-1.8976` n `162`; fx avg `0.041` n `6`; index avg `-0.21` n `27`; metal avg `-0.0653` n `20`; unknown avg `1.0437` n `1242`
- 24h: commodity avg `0.834` n `13`; crypto_alt avg `-3.0032` n `239`; crypto_major avg `-4.3817` n `8`; equity avg `-1.0785` n `162`; fx avg `0.0186` n `6`; index avg `0.0028` n `27`; metal avg `-0.4321` n `20`; unknown avg `99.5715` n `1121`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
