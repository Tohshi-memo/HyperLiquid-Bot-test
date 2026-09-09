# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T21:52:32.224583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6377` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `-0.5686` n `233`; crypto_major avg `-0.3086` n `8`; equity avg `-0.0631` n `134`; fx avg `-0.0019` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0131` n `20`; unknown avg `11.7511` n `789`
- 1h: commodity avg `0.0328` n `12`; crypto_alt avg `-0.9783` n `233`; crypto_major avg `-0.436` n `8`; equity avg `-0.1731` n `134`; fx avg `0.0025` n `6`; index avg `-0.0069` n `26`; metal avg `0.0001` n `20`; unknown avg `130.3965` n `773`
- 4h: commodity avg `0.1375` n `12`; crypto_alt avg `-2.313` n `233`; crypto_major avg `-1.657` n `8`; equity avg `-0.5168` n `134`; fx avg `-0.0164` n `6`; index avg `-0.0193` n `26`; metal avg `-0.1682` n `20`; unknown avg `3.1783` n `743`
- 24h: commodity avg `0.0966` n `12`; crypto_alt avg `-2.0787` n `233`; crypto_major avg `-1.2941` n `8`; equity avg `-0.553` n `134`; fx avg `-0.0063` n `6`; index avg `-0.1364` n `26`; metal avg `0.4749` n `20`; unknown avg `8.2329` n `693`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
