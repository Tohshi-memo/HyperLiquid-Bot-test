# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T12:07:27.005670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `13`; crypto_alt avg `-0.0187` n `239`; crypto_major avg `-0.0216` n `8`; equity avg `0.0059` n `162`; fx avg `0.0018` n `6`; index avg `0.0008` n `27`; metal avg `0.0053` n `20`; unknown avg `0.3097` n `1250`
- 1h: commodity avg `-0.022` n `13`; crypto_alt avg `0.241` n `239`; crypto_major avg `0.1329` n `8`; equity avg `0.0333` n `162`; fx avg `0.0063` n `6`; index avg `0.0042` n `27`; metal avg `0.0054` n `20`; unknown avg `159.8808` n `1252`
- 4h: commodity avg `-0.0511` n `13`; crypto_alt avg `-0.2551` n `239`; crypto_major avg `0.1157` n `8`; equity avg `0.042` n `162`; fx avg `0.0018` n `6`; index avg `-0.0025` n `27`; metal avg `0.0179` n `20`; unknown avg `85.7566` n `1176`
- 24h: commodity avg `-0.2254` n `13`; crypto_alt avg `-3.3591` n `239`; crypto_major avg `-3.6492` n `8`; equity avg `-3.2677` n `162`; fx avg `-0.1325` n `6`; index avg `-0.2853` n `27`; metal avg `-0.3967` n `20`; unknown avg `1.7576` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
