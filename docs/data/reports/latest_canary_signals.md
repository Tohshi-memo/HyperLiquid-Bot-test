# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T19:09:24.228246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0037` n `13`; crypto_alt avg `0.0533` n `239`; crypto_major avg `-0.081` n `8`; equity avg `-0.1781` n `158`; fx avg `0.012` n `6`; index avg `-0.0176` n `27`; metal avg `-0.0052` n `20`; unknown avg `159.2436` n `1257`
- 1h: commodity avg `0.0163` n `13`; crypto_alt avg `-0.2295` n `239`; crypto_major avg `-0.5045` n `8`; equity avg `-0.4595` n `158`; fx avg `0.0106` n `6`; index avg `-0.0601` n `27`; metal avg `-0.0638` n `20`; unknown avg `1.3164` n `1257`
- 4h: commodity avg `0.1814` n `13`; crypto_alt avg `-0.034` n `239`; crypto_major avg `-0.0934` n `8`; equity avg `-0.1905` n `158`; fx avg `0.0358` n `6`; index avg `-0.0241` n `27`; metal avg `-0.1584` n `20`; unknown avg `-0.4039` n `1215`
- 24h: commodity avg `0.1712` n `13`; crypto_alt avg `1.1824` n `239`; crypto_major avg `1.4732` n `8`; equity avg `0.8393` n `158`; fx avg `0.0906` n `6`; index avg `0.036` n `27`; metal avg `-0.5413` n `20`; unknown avg `371.1665` n `1059`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
