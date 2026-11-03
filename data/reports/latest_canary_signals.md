# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T18:22:43.629117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0414` n `13`; crypto_alt avg `-0.2496` n `239`; crypto_major avg `-0.2327` n `8`; equity avg `-0.2727` n `158`; fx avg `-0.0015` n `6`; index avg `-0.0342` n `27`; metal avg `-0.021` n `20`; unknown avg `1.4223` n `1261`
- 1h: commodity avg `-0.0499` n `13`; crypto_alt avg `-0.2126` n `239`; crypto_major avg `-0.0602` n `8`; equity avg `-0.0831` n `158`; fx avg `0.0082` n `6`; index avg `0.0015` n `27`; metal avg `0.0018` n `20`; unknown avg `0.0411` n `1219`
- 4h: commodity avg `0.161` n `13`; crypto_alt avg `0.125` n `239`; crypto_major avg `0.3273` n `8`; equity avg `0.5808` n `158`; fx avg `0.0688` n `6`; index avg `0.0262` n `27`; metal avg `-0.1962` n `20`; unknown avg `0.0045` n `1215`
- 24h: commodity avg `0.1765` n `13`; crypto_alt avg `0.8066` n `239`; crypto_major avg `1.4899` n `8`; equity avg `0.0984` n `158`; fx avg `0.0766` n `6`; index avg `-0.0244` n `27`; metal avg `-0.5976` n `20`; unknown avg `374.605` n `1049`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
