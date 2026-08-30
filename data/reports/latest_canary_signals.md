# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T18:37:27.150252+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `0.2733` n `231`; crypto_major avg `0.3836` n `8`; equity avg `0.0351` n `128`; fx avg `0.0028` n `6`; index avg `-0.0116` n `26`; metal avg `0.0094` n `20`; unknown avg `0.0447` n `793`
- 1h: commodity avg `0.0127` n `12`; crypto_alt avg `0.2761` n `231`; crypto_major avg `0.4787` n `8`; equity avg `0.0164` n `128`; fx avg `-0.001` n `6`; index avg `-0.0093` n `26`; metal avg `-0.0132` n `20`; unknown avg `-0.1182` n `793`
- 4h: commodity avg `0.0748` n `12`; crypto_alt avg `0.6646` n `231`; crypto_major avg `0.7171` n `8`; equity avg `0.1234` n `128`; fx avg `0.0052` n `6`; index avg `0.0176` n `26`; metal avg `0.0282` n `20`; unknown avg `0.293` n `793`
- 24h: commodity avg `0.0385` n `12`; crypto_alt avg `1.8613` n `231`; crypto_major avg `1.4508` n `8`; equity avg `0.3988` n `128`; fx avg `0.0254` n `6`; index avg `0.0921` n `26`; metal avg `0.1194` n `20`; unknown avg `0.0331` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
