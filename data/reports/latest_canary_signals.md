# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T07:52:19.292526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.9334` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.8196` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.7543` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1994` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0396` n `12`; crypto_alt avg `-1.7362` n `228`; crypto_major avg `-1.2391` n `8`; equity avg `-0.0627` n `67`; fx avg `-0.0087` n `6`; index avg `-0.0655` n `23`; metal avg `-0.1075` n `18`; unknown avg `-0.6175` n `386`
- 1h: commodity avg `-0.119` n `12`; crypto_alt avg `-1.9184` n `228`; crypto_major avg `-1.3207` n `8`; equity avg `-0.0649` n `67`; fx avg `-0.0004` n `6`; index avg `-0.1213` n `23`; metal avg `-0.0436` n `18`; unknown avg `-0.4394` n `386`
- 4h: commodity avg `-0.128` n `12`; crypto_alt avg `-2.8558` n `228`; crypto_major avg `-1.9805` n `8`; equity avg `-0.1609` n `67`; fx avg `0.0081` n `6`; index avg `-0.2262` n `23`; metal avg `-0.0471` n `18`; unknown avg `-0.9274` n `376`
- 24h: commodity avg `-0.534` n `12`; crypto_alt avg `-6.1836` n `228`; crypto_major avg `-4.1275` n `8`; equity avg `-2.0015` n `67`; fx avg `0.0716` n `6`; index avg `-0.281` n `23`; metal avg `-0.5008` n `18`; unknown avg `-2.942` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
