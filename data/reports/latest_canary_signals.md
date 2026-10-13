# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T01:07:41.091629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.587` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.4625` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.3639` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.041` n `13`; crypto_alt avg `1.2787` n `235`; crypto_major avg `1.0829` n `8`; equity avg `0.0031` n `151`; fx avg `0.0311` n `6`; index avg `-0.0233` n `26`; metal avg `0.0461` n `20`; unknown avg `0.863` n `1133`
- 1h: commodity avg `-0.0283` n `13`; crypto_alt avg `-0.6873` n `235`; crypto_major avg `-0.0024` n `8`; equity avg `-0.1295` n `151`; fx avg `0.0144` n `6`; index avg `-0.063` n `26`; metal avg `-0.0087` n `20`; unknown avg `-0.1391` n `1133`
- 4h: commodity avg `0.0199` n `13`; crypto_alt avg `-3.7069` n `235`; crypto_major avg `-2.5671` n `8`; equity avg `-1.3335` n `151`; fx avg `0.0477` n `6`; index avg `-0.2032` n `26`; metal avg `-0.1046` n `20`; unknown avg `4.7366` n `1089`
- 24h: commodity avg `0.7515` n `13`; crypto_alt avg `-6.6882` n `235`; crypto_major avg `-4.5509` n `8`; equity avg `-4.7445` n `151`; fx avg `-0.0558` n `6`; index avg `-0.5354` n `26`; metal avg `-0.3199` n `20`; unknown avg `0.5574` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2062`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1843`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1201`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1038`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0956`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0874`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `666`, weak_sample_signal
