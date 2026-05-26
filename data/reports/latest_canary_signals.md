# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T03:07:17.709004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0762` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0075` n `12`; crypto_alt avg `-0.3083` n `228`; crypto_major avg `-0.2189` n `8`; equity avg `-0.0037` n `67`; fx avg `-0.0064` n `6`; index avg `0.0014` n `23`; metal avg `0.041` n `18`; unknown avg `-0.7502` n `407`
- 1h: commodity avg `-0.097` n `12`; crypto_alt avg `-0.1499` n `228`; crypto_major avg `-0.2051` n `8`; equity avg `0.0203` n `67`; fx avg `0.0029` n `6`; index avg `-0.0194` n `23`; metal avg `0.0306` n `18`; unknown avg `-0.5099` n `407`
- 4h: commodity avg `0.3154` n `12`; crypto_alt avg `-1.5515` n `228`; crypto_major avg `-1.311` n `8`; equity avg `-0.7321` n `67`; fx avg `-0.112` n `6`; index avg `-0.2348` n `23`; metal avg `-1.0538` n `18`; unknown avg `-0.6909` n `405`
- 24h: commodity avg `0.158` n `12`; crypto_alt avg `-0.3484` n `228`; crypto_major avg `-1.096` n `8`; equity avg `-0.3263` n `67`; fx avg `0.003` n `6`; index avg `0.0125` n `23`; metal avg `-0.1403` n `18`; unknown avg `0.2292` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
