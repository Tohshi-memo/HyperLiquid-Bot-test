# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T18:37:39.510338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6176` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7726` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6515` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.082` n `13`; crypto_alt avg `-0.863` n `235`; crypto_major avg `-0.5078` n `8`; equity avg `-0.0428` n `143`; fx avg `-0.0071` n `6`; index avg `-0.0062` n `26`; metal avg `0.0412` n `20`; unknown avg `11.2314` n `984`
- 1h: commodity avg `0.018` n `13`; crypto_alt avg `-1.8471` n `235`; crypto_major avg `-0.8841` n `8`; equity avg `-0.0004` n `143`; fx avg `-0.0116` n `6`; index avg `-0.0015` n `26`; metal avg `0.061` n `20`; unknown avg `0.8282` n `982`
- 4h: commodity avg `0.6813` n `13`; crypto_alt avg `-3.0545` n `235`; crypto_major avg `-1.9363` n `8`; equity avg `-0.9318` n `143`; fx avg `-0.0024` n `6`; index avg `-0.1637` n `26`; metal avg `-0.2848` n `20`; unknown avg `2.3939` n `974`
- 24h: commodity avg `-0.1663` n `13`; crypto_alt avg `-1.4191` n `235`; crypto_major avg `-0.9972` n `8`; equity avg `0.5686` n `142`; fx avg `-0.1239` n `6`; index avg `0.2633` n `26`; metal avg `-0.2714` n `20`; unknown avg `99.6693` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
