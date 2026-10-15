# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T13:52:28.002719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5743` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5671` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1179` n `13`; crypto_alt avg `-0.326` n `236`; crypto_major avg `-0.3752` n `8`; equity avg `-0.2341` n `151`; fx avg `0.0026` n `6`; index avg `-0.0445` n `26`; metal avg `-0.1116` n `20`; unknown avg `-0.0527` n `1136`
- 1h: commodity avg `0.0136` n `13`; crypto_alt avg `-0.6332` n `236`; crypto_major avg `-0.8661` n `8`; equity avg `-0.8221` n `151`; fx avg `-0.0188` n `6`; index avg `-0.0885` n `26`; metal avg `-0.0182` n `20`; unknown avg `-0.4203` n `1134`
- 4h: commodity avg `-0.0353` n `13`; crypto_alt avg `-1.3775` n `236`; crypto_major avg `-1.6594` n `8`; equity avg `-1.2762` n `151`; fx avg `-0.0118` n `6`; index avg `-0.0851` n `26`; metal avg `-0.0923` n `20`; unknown avg `0.5687` n `1056`
- 24h: commodity avg `-0.3793` n `13`; crypto_alt avg `-4.553` n `236`; crypto_major avg `-3.8003` n `8`; equity avg `-5.4762` n `151`; fx avg `0.1357` n `6`; index avg `-0.828` n `26`; metal avg `0.0584` n `20`; unknown avg `-0.3368` n `957`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1205`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0976`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.096`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0913`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.081`, n `666`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.078`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
