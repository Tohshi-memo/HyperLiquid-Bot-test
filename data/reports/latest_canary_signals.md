# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T23:07:30.305284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.2538` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.1795` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.9848` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.01` n `13`; crypto_alt avg `-0.4016` n `238`; crypto_major avg `-0.2395` n `8`; equity avg `-0.0699` n `156`; fx avg `0.0009` n `6`; index avg `-0.0078` n `27`; metal avg `-0.0442` n `20`; unknown avg `7.177` n `1254`
- 1h: commodity avg `-0.0275` n `13`; crypto_alt avg `0.2641` n `238`; crypto_major avg `-0.0625` n `8`; equity avg `-0.4378` n `156`; fx avg `0.0231` n `6`; index avg `-0.0606` n `27`; metal avg `-0.0692` n `20`; unknown avg `5.8691` n `1252`
- 4h: commodity avg `0.0488` n `13`; crypto_alt avg `-4.7535` n `238`; crypto_major avg `-3.205` n `8`; equity avg `-2.5708` n `156`; fx avg `0.0476` n `6`; index avg `-0.2202` n `27`; metal avg `-0.0255` n `20`; unknown avg `194.9029` n `1162`
- 24h: commodity avg `-0.211` n `13`; crypto_alt avg `-6.0338` n `238`; crypto_major avg `-2.3577` n `8`; equity avg `-3.689` n `155`; fx avg `0.0858` n `6`; index avg `-0.3323` n `27`; metal avg `-0.6293` n `20`; unknown avg `31.6821` n `996`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
