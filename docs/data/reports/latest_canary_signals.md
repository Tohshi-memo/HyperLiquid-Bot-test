# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T16:37:32.654606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0573` n `13`; crypto_alt avg `0.146` n `237`; crypto_major avg `0.0567` n `8`; equity avg `-0.0925` n `151`; fx avg `-0.0003` n `6`; index avg `-0.0206` n `26`; metal avg `0.0138` n `20`; unknown avg `-0.0766` n `1196`
- 1h: commodity avg `0.1963` n `13`; crypto_alt avg `0.1372` n `237`; crypto_major avg `-0.0889` n `8`; equity avg `-0.6206` n `151`; fx avg `-0.013` n `6`; index avg `-0.1136` n `26`; metal avg `-0.0336` n `20`; unknown avg `-0.1139` n `1188`
- 4h: commodity avg `0.1065` n `13`; crypto_alt avg `0.03` n `237`; crypto_major avg `-0.6945` n `8`; equity avg `-0.4176` n `151`; fx avg `0.021` n `6`; index avg `0.0102` n `26`; metal avg `-0.1261` n `20`; unknown avg `-0.1298` n `1119`
- 24h: commodity avg `-0.1341` n `13`; crypto_alt avg `1.6948` n `237`; crypto_major avg `1.7345` n `8`; equity avg `3.1553` n `151`; fx avg `-0.0239` n `6`; index avg `0.5947` n `26`; metal avg `0.109` n `20`; unknown avg `2.8387` n `916`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2103`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
