# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T23:37:44.673848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5926` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5659` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0032` n `13`; crypto_alt avg `0.2752` n `239`; crypto_major avg `0.2703` n `8`; equity avg `-0.0201` n `162`; fx avg `-0.0058` n `6`; index avg `0.0039` n `27`; metal avg `0.0061` n `20`; unknown avg `0.4358` n `1262`
- 1h: commodity avg `0.0095` n `13`; crypto_alt avg `-0.0099` n `239`; crypto_major avg `-0.2527` n `8`; equity avg `-0.2628` n `162`; fx avg `-0.0063` n `6`; index avg `-0.0135` n `27`; metal avg `-0.0089` n `20`; unknown avg `0.004` n `1210`
- 4h: commodity avg `0.059` n `13`; crypto_alt avg `-1.304` n `239`; crypto_major avg `-1.6137` n `8`; equity avg `-0.9694` n `162`; fx avg `-0.0072` n `6`; index avg `-0.0478` n `27`; metal avg `-0.0211` n `20`; unknown avg `3.7165` n `1162`
- 24h: commodity avg `-0.3238` n `13`; crypto_alt avg `-1.5783` n `239`; crypto_major avg `-3.0884` n `8`; equity avg `-3.9002` n `162`; fx avg `-0.0795` n `6`; index avg `-0.3045` n `27`; metal avg `-0.3408` n `20`; unknown avg `64.1291` n `1035`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
