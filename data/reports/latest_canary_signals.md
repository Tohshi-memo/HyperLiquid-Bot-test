# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T03:22:29.535817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.859` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3202` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0029` n `13`; crypto_alt avg `-0.1578` n `236`; crypto_major avg `-0.2157` n `8`; equity avg `-0.1017` n `151`; fx avg `-0.0381` n `6`; index avg `-0.0097` n `26`; metal avg `-0.0328` n `20`; unknown avg `-0.2` n `1136`
- 1h: commodity avg `-0.0015` n `13`; crypto_alt avg `-0.445` n `236`; crypto_major avg `-0.2348` n `8`; equity avg `-0.3516` n `151`; fx avg `0.0097` n `6`; index avg `-0.0962` n `26`; metal avg `0.0153` n `20`; unknown avg `1.1665` n `1134`
- 4h: commodity avg `-0.2564` n `13`; crypto_alt avg `-2.927` n `236`; crypto_major avg `-1.656` n `8`; equity avg `-0.6289` n `151`; fx avg `0.1845` n `6`; index avg `-0.3358` n `26`; metal avg `0.203` n `20`; unknown avg `1.4923` n `1128`
- 24h: commodity avg `-0.4509` n `13`; crypto_alt avg `-5.4652` n `236`; crypto_major avg `-4.0868` n `8`; equity avg `-6.3447` n `151`; fx avg `0.0861` n `6`; index avg `-1.0973` n `26`; metal avg `-0.7251` n `20`; unknown avg `1396.1021` n `890`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1432`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1415`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1082`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1045`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.099`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0953`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0849`, n `666`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0806`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
