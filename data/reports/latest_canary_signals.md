# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T02:07:41.335449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3021` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7624` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7299` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0874` n `13`; crypto_alt avg `-0.1624` n `238`; crypto_major avg `0.1031` n `8`; equity avg `0.0898` n `156`; fx avg `-0.01` n `6`; index avg `0.0136` n `27`; metal avg `0.1044` n `20`; unknown avg `3.7289` n `1254`
- 1h: commodity avg `0.3871` n `13`; crypto_alt avg `-0.6474` n `238`; crypto_major avg `-0.5211` n `8`; equity avg `0.0176` n `156`; fx avg `-0.025` n `6`; index avg `-0.0409` n `27`; metal avg `0.0672` n `20`; unknown avg `3.816` n `1254`
- 4h: commodity avg `0.3086` n `13`; crypto_alt avg `-2.4674` n `238`; crypto_major avg `-1.9935` n `8`; equity avg `-1.241` n `156`; fx avg `-0.0088` n `6`; index avg `-0.2311` n `27`; metal avg `-0.2636` n `20`; unknown avg `9.9231` n `1238`
- 24h: commodity avg `0.1108` n `13`; crypto_alt avg `-6.3341` n `238`; crypto_major avg `-2.3787` n `8`; equity avg `-3.4223` n `155`; fx avg `0.1417` n `6`; index avg `-0.3307` n `27`; metal avg `-0.7537` n `20`; unknown avg `32.5241` n `988`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
