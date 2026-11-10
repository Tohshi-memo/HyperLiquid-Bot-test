# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T17:07:37.653990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.3291` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.6156` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.4152` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0302` n `13`; crypto_alt avg `-0.5588` n `239`; crypto_major avg `-0.2205` n `8`; equity avg `-0.2394` n `160`; fx avg `0.0071` n `6`; index avg `-0.0471` n `27`; metal avg `0.019` n `20`; unknown avg `18.4325` n `1258`
- 1h: commodity avg `0.4522` n `13`; crypto_alt avg `-1.0368` n `239`; crypto_major avg `-0.5651` n `8`; equity avg `-1.1745` n `160`; fx avg `-0.009` n `6`; index avg `-0.1329` n `27`; metal avg `-0.1151` n `20`; unknown avg `18.2789` n `1256`
- 4h: commodity avg `0.5532` n `13`; crypto_alt avg `-2.0212` n `239`; crypto_major avg `-2.7759` n `8`; equity avg `-1.3282` n `160`; fx avg `-0.092` n `6`; index avg `-0.1603` n `27`; metal avg `-0.3607` n `20`; unknown avg `18.3401` n `1250`
- 24h: commodity avg `-0.1429` n `13`; crypto_alt avg `-2.7735` n `239`; crypto_major avg `-3.8752` n `8`; equity avg `-2.2941` n `160`; fx avg `-0.1187` n `6`; index avg `-0.1964` n `27`; metal avg `-0.4986` n `20`; unknown avg `20.6477` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2401`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
