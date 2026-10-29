# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T03:07:32.897624+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6882` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6132` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0196` n `13`; crypto_alt avg `0.1823` n `238`; crypto_major avg `0.0818` n `8`; equity avg `0.0034` n `155`; fx avg `-0.0043` n `6`; index avg `-0.0038` n `27`; metal avg `-0.0885` n `20`; unknown avg `1.8177` n `1228`
- 1h: commodity avg `-0.0265` n `13`; crypto_alt avg `-0.076` n `238`; crypto_major avg `0.052` n `8`; equity avg `-0.022` n `155`; fx avg `-0.0212` n `6`; index avg `0.0168` n `27`; metal avg `-0.1641` n `20`; unknown avg `1.5705` n `1222`
- 4h: commodity avg `-0.0079` n `13`; crypto_alt avg `-2.479` n `238`; crypto_major avg `-1.8448` n `8`; equity avg `-1.1198` n `155`; fx avg `-0.1088` n `6`; index avg `-0.1566` n `27`; metal avg `-0.2316` n `20`; unknown avg `190.4632` n `1200`
- 24h: commodity avg `-0.0455` n `13`; crypto_alt avg `-2.3681` n `238`; crypto_major avg `-1.5982` n `8`; equity avg `-1.1157` n `154`; fx avg `-0.0019` n `6`; index avg `-0.1379` n `27`; metal avg `-0.2392` n `20`; unknown avg `30.772` n `986`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
