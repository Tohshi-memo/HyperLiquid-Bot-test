# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T23:22:25.613423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0262` n `13`; crypto_alt avg `0.0971` n `236`; crypto_major avg `0.0304` n `8`; equity avg `0.1038` n `151`; fx avg `0.0015` n `6`; index avg `0.0298` n `26`; metal avg `0.0094` n `20`; unknown avg `-0.0015` n `1193`
- 1h: commodity avg `-0.0159` n `13`; crypto_alt avg `0.2082` n `236`; crypto_major avg `0.0593` n `8`; equity avg `0.1852` n `151`; fx avg `0.0078` n `6`; index avg `0.03` n `26`; metal avg `0.0288` n `20`; unknown avg `0.4623` n `1191`
- 4h: commodity avg `-0.063` n `13`; crypto_alt avg `-0.9181` n `236`; crypto_major avg `-0.6237` n `8`; equity avg `-0.847` n `151`; fx avg `0.0021` n `6`; index avg `-0.1068` n `26`; metal avg `-0.0464` n `20`; unknown avg `0.3473` n `1147`
- 24h: commodity avg `-0.0193` n `13`; crypto_alt avg `-2.3664` n `236`; crypto_major avg `-1.3011` n `8`; equity avg `-0.5546` n `151`; fx avg `-0.0279` n `6`; index avg `-0.076` n `26`; metal avg `-0.0803` n `20`; unknown avg `4.2688` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1643`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1377`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.106`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1051`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.073`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
