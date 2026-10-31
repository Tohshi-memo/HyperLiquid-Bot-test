# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T10:22:23.139469+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `13`; crypto_alt avg `0.1254` n `238`; crypto_major avg `0.1763` n `8`; equity avg `0.0054` n `156`; fx avg `0.0126` n `6`; index avg `-0.0006` n `27`; metal avg `0.006` n `20`; unknown avg `0.0383` n `1262`
- 1h: commodity avg `-0.0334` n `13`; crypto_alt avg `0.0437` n `238`; crypto_major avg `0.1372` n `8`; equity avg `-0.0102` n `156`; fx avg `0.0177` n `6`; index avg `0.0049` n `27`; metal avg `0.0139` n `20`; unknown avg `0.0868` n `1256`
- 4h: commodity avg `-0.0468` n `13`; crypto_alt avg `-0.3026` n `238`; crypto_major avg `-0.0672` n `8`; equity avg `-0.02` n `156`; fx avg `0.0195` n `6`; index avg `-0.0083` n `27`; metal avg `0.0098` n `20`; unknown avg `5.1588` n `1232`
- 24h: commodity avg `-0.2985` n `13`; crypto_alt avg `0.5942` n `238`; crypto_major avg `-0.5693` n `8`; equity avg `-1.6808` n `156`; fx avg `-0.0924` n `6`; index avg `-0.1511` n `27`; metal avg `-0.3801` n `20`; unknown avg `4.676` n `1043`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
