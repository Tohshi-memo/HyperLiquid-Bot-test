# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T16:52:46.375819+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0235` n `13`; crypto_alt avg `0.0577` n `239`; crypto_major avg `0.0958` n `8`; equity avg `-0.0021` n `158`; fx avg `0.0094` n `6`; index avg `-0.0028` n `27`; metal avg `-0.0404` n `20`; unknown avg `-0.0142` n `1263`
- 1h: commodity avg `0.1133` n `13`; crypto_alt avg `-0.1108` n `239`; crypto_major avg `-0.1537` n `8`; equity avg `-0.4174` n `158`; fx avg `0.0157` n `6`; index avg `-0.0492` n `27`; metal avg `-0.1166` n `20`; unknown avg `0.2051` n `1251`
- 4h: commodity avg `-0.2038` n `13`; crypto_alt avg `-0.2534` n `239`; crypto_major avg `0.175` n `8`; equity avg `0.5992` n `158`; fx avg `0.0611` n `6`; index avg `0.0536` n `27`; metal avg `-0.1113` n `20`; unknown avg `21.8615` n `1251`
- 24h: commodity avg `-0.0506` n `13`; crypto_alt avg `-0.1002` n `239`; crypto_major avg `0.5609` n `8`; equity avg `-0.8051` n `158`; fx avg `0.0521` n `6`; index avg `-0.1047` n `27`; metal avg `-0.6803` n `20`; unknown avg `0.128` n `1021`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
