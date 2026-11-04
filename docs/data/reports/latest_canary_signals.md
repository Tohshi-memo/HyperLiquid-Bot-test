# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T02:41:44.308629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.16` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.6974` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.2051` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0696` n `13`; crypto_alt avg `-0.3188` n `239`; crypto_major avg `-0.2824` n `8`; equity avg `-0.4422` n `158`; fx avg `-0.0088` n `6`; index avg `-0.1102` n `27`; metal avg `-0.0225` n `20`; unknown avg `-0.196` n `1262`
- 1h: commodity avg `-0.2949` n `13`; crypto_alt avg `-0.2937` n `239`; crypto_major avg `-0.3317` n `8`; equity avg `-0.5281` n `158`; fx avg `-0.0264` n `6`; index avg `-0.1611` n `27`; metal avg `-0.2858` n `20`; unknown avg `-0.2827` n `1256`
- 4h: commodity avg `-0.4729` n `13`; crypto_alt avg `-1.677` n `239`; crypto_major avg `-1.8009` n `8`; equity avg `-3.0842` n `158`; fx avg `-0.0406` n `6`; index avg `-0.5958` n `27`; metal avg `-0.1035` n `20`; unknown avg `148.3361` n `1196`
- 24h: commodity avg `-0.2168` n `13`; crypto_alt avg `-0.3514` n `239`; crypto_major avg `-0.7515` n `8`; equity avg `-1.16` n `158`; fx avg `0.1097` n `6`; index avg `-0.4135` n `27`; metal avg `-0.478` n `20`; unknown avg `-0.2745` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
