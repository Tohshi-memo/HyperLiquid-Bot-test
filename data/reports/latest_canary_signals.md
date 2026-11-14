# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T21:07:33.252811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-2.0937` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.076` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.7471` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.7262` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0307` n `13`; crypto_alt avg `-0.8402` n `239`; crypto_major avg `-0.8165` n `8`; equity avg `-0.3571` n `162`; fx avg `-0.0015` n `6`; index avg `-0.0256` n `27`; metal avg `-0.2654` n `20`; unknown avg `0.0161` n `1238`
- 1h: commodity avg `-0.0268` n `13`; crypto_alt avg `-2.3222` n `239`; crypto_major avg `-2.1205` n `8`; equity avg `-0.7614` n `162`; fx avg `0.007` n `6`; index avg `-0.0445` n `27`; metal avg `-0.3943` n `20`; unknown avg `2.1572` n `1224`
- 4h: commodity avg `0.0159` n `13`; crypto_alt avg `-2.7966` n `239`; crypto_major avg `-1.7774` n `8`; equity avg `-0.5941` n `162`; fx avg `-0.001` n `6`; index avg `-0.0303` n `27`; metal avg `-0.3773` n `20`; unknown avg `0.296` n `1214`
- 24h: commodity avg `-0.1092` n `13`; crypto_alt avg `-9.2224` n `239`; crypto_major avg `-8.3909` n `8`; equity avg `-2.332` n `162`; fx avg `-0.035` n `6`; index avg `-0.1768` n `27`; metal avg `-0.6016` n `20`; unknown avg `0.8736` n `1098`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
