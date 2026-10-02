# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T20:22:35.195340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2872` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.9743` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8528` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.7141` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0025` n `13`; crypto_alt avg `-0.0241` n `235`; crypto_major avg `-0.0037` n `8`; equity avg `-0.0246` n `143`; fx avg `-0.0115` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0042` n `20`; unknown avg `1.5177` n `954`
- 1h: commodity avg `0.1968` n `13`; crypto_alt avg `0.3385` n `235`; crypto_major avg `0.3043` n `8`; equity avg `0.0903` n `143`; fx avg `-0.0165` n `6`; index avg `0.0306` n `26`; metal avg `0.0069` n `20`; unknown avg `10.5181` n `934`
- 4h: commodity avg `0.4393` n `13`; crypto_alt avg `-3.7424` n `235`; crypto_major avg `-1.8479` n `8`; equity avg `-0.1338` n `143`; fx avg `-0.0047` n `6`; index avg `0.0049` n `26`; metal avg `0.1264` n `20`; unknown avg `0.891` n `934`
- 24h: commodity avg `0.0056` n `13`; crypto_alt avg `-2.0371` n `235`; crypto_major avg `-1.1964` n `8`; equity avg `0.7132` n `142`; fx avg `-0.1399` n `6`; index avg `0.2935` n `26`; metal avg `-0.2236` n `20`; unknown avg `-0.1623` n `804`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
