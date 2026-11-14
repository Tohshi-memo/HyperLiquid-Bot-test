# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T17:07:23.768985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `3.4117` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.4037` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.2827` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.5614` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.394` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.009` n `13`; crypto_alt avg `-0.2947` n `239`; crypto_major avg `-0.5316` n `8`; equity avg `-0.0416` n `162`; fx avg `-0.0061` n `6`; index avg `0.0121` n `27`; metal avg `-0.0235` n `20`; unknown avg `1.6127` n `1256`
- 1h: commodity avg `-0.0568` n `13`; crypto_alt avg `-1.2044` n `239`; crypto_major avg `-1.4272` n `8`; equity avg `-0.3822` n `162`; fx avg `-0.0003` n `6`; index avg `-0.0332` n `27`; metal avg `-0.0274` n `20`; unknown avg `0.0363` n `1260`
- 4h: commodity avg `-0.0955` n `13`; crypto_alt avg `-3.5863` n `239`; crypto_major avg `-3.4992` n `8`; equity avg `-0.9378` n `162`; fx avg `0.0108` n `6`; index avg `-0.0875` n `27`; metal avg `-0.2165` n `20`; unknown avg `161.7689` n `1250`
- 24h: commodity avg `0.0402` n `13`; crypto_alt avg `-6.7507` n `239`; crypto_major avg `-6.6748` n `8`; equity avg `-1.6457` n `162`; fx avg `-0.068` n `6`; index avg `-0.1042` n `27`; metal avg `-0.3644` n `20`; unknown avg `3.1893` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
