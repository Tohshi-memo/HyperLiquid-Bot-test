# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T11:37:26.166771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2112` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.8427` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7131` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0039` n `12`; crypto_alt avg `-0.3003` n `234`; crypto_major avg `-0.2352` n `8`; equity avg `-0.0826` n `141`; fx avg `0.0004` n `6`; index avg `-0.023` n `26`; metal avg `-0.0341` n `20`; unknown avg `3.844` n `945`
- 1h: commodity avg `0.0376` n `12`; crypto_alt avg `0.6419` n `234`; crypto_major avg `0.4397` n `8`; equity avg `0.1264` n `141`; fx avg `-0.0028` n `6`; index avg `0.0202` n `26`; metal avg `0.0225` n `20`; unknown avg `3.7022` n `943`
- 4h: commodity avg `0.2554` n `12`; crypto_alt avg `-1.662` n `234`; crypto_major avg `-1.9558` n `8`; equity avg `-0.6652` n `141`; fx avg `0.0369` n `6`; index avg `-0.1131` n `26`; metal avg `-0.2427` n `20`; unknown avg `1.2691` n `937`
- 24h: commodity avg `0.5011` n `12`; crypto_alt avg `-3.8627` n `234`; crypto_major avg `-3.4237` n `8`; equity avg `-1.8845` n `141`; fx avg `0.0312` n `6`; index avg `-0.3953` n `26`; metal avg `-0.2992` n `20`; unknown avg `586.8993` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
