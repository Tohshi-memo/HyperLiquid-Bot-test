# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T23:37:24.741660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.3043` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.2144` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.0535` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0046` n `13`; crypto_alt avg `-0.4167` n `238`; crypto_major avg `-0.2407` n `8`; equity avg `0.0026` n `156`; fx avg `0.0024` n `6`; index avg `-0.0041` n `27`; metal avg `-0.0083` n `20`; unknown avg `1.2839` n `1260`
- 1h: commodity avg `-0.0304` n `13`; crypto_alt avg `-0.9675` n `238`; crypto_major avg `-0.7986` n `8`; equity avg `-0.2198` n `156`; fx avg `0.0004` n `6`; index avg `-0.0179` n `27`; metal avg `-0.0693` n `20`; unknown avg `6.3783` n `1254`
- 4h: commodity avg `0.0203` n `13`; crypto_alt avg `-5.0177` n `238`; crypto_major avg `-3.284` n `8`; equity avg `-2.6323` n `156`; fx avg `0.0189` n `6`; index avg `-0.2305` n `27`; metal avg `-0.0696` n `20`; unknown avg `23.264` n `1162`
- 24h: commodity avg `-0.1923` n `13`; crypto_alt avg `-6.0607` n `238`; crypto_major avg `-2.4821` n `8`; equity avg `-3.3556` n `155`; fx avg `0.0806` n `6`; index avg `-0.2623` n `27`; metal avg `-0.6355` n `20`; unknown avg `29.8104` n `996`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
