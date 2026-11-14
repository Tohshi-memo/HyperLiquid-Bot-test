# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T09:22:26.172387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `13`; crypto_alt avg `-0.1659` n `239`; crypto_major avg `-0.1463` n `8`; equity avg `-0.0154` n `162`; fx avg `-0.0053` n `6`; index avg `-0.0061` n `27`; metal avg `-0.0002` n `20`; unknown avg `202.9616` n `1230`
- 1h: commodity avg `-0.0188` n `13`; crypto_alt avg `-0.2089` n `239`; crypto_major avg `-0.2261` n `8`; equity avg `-0.027` n `162`; fx avg `-0.0069` n `6`; index avg `-0.0125` n `27`; metal avg `0.0089` n `20`; unknown avg `207.6363` n `1210`
- 4h: commodity avg `0.0273` n `13`; crypto_alt avg `-1.0648` n `239`; crypto_major avg `-0.4089` n `8`; equity avg `0.0358` n `162`; fx avg `-0.007` n `6`; index avg `-0.0048` n `27`; metal avg `0.025` n `20`; unknown avg `214.5213` n `1176`
- 24h: commodity avg `-0.184` n `13`; crypto_alt avg `-2.718` n `239`; crypto_major avg `-3.0329` n `8`; equity avg `-2.6156` n `162`; fx avg `-0.1574` n `6`; index avg `-0.2216` n `27`; metal avg `-0.343` n `20`; unknown avg `1.441` n `1042`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
