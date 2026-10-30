# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T01:52:29.084753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.9992` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3251` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.2421` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.2657` n `13`; crypto_alt avg `-0.6293` n `238`; crypto_major avg `-0.4648` n `8`; equity avg `-0.396` n `156`; fx avg `-0.0079` n `6`; index avg `-0.0556` n `27`; metal avg `-0.0794` n `20`; unknown avg `7.2259` n `1260`
- 1h: commodity avg `0.4517` n `13`; crypto_alt avg `-0.7502` n `238`; crypto_major avg `-0.8142` n `8`; equity avg `-0.5609` n `156`; fx avg `-0.028` n `6`; index avg `-0.1361` n `27`; metal avg `-0.3142` n `20`; unknown avg `4.4064` n `1254`
- 4h: commodity avg `0.418` n `13`; crypto_alt avg `-3.2531` n `238`; crypto_major avg `-2.5812` n `8`; equity avg `-1.3697` n `156`; fx avg `0.0118` n `6`; index avg `-0.2561` n `27`; metal avg `-0.3391` n `20`; unknown avg `6.3947` n `1238`
- 24h: commodity avg `0.1315` n `13`; crypto_alt avg `-6.8246` n `238`; crypto_major avg `-2.8075` n `8`; equity avg `-3.5952` n `155`; fx avg `0.1994` n `6`; index avg `-0.3312` n `27`; metal avg `-0.8436` n `20`; unknown avg `32.6431` n `988`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
