# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T08:52:28.335783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0665` n `13`; crypto_alt avg `-0.1301` n `237`; crypto_major avg `-0.0868` n `8`; equity avg `-0.062` n `151`; fx avg `0.0101` n `6`; index avg `-0.0248` n `26`; metal avg `-0.0123` n `20`; unknown avg `0.0489` n `1195`
- 1h: commodity avg `0.122` n `13`; crypto_alt avg `-0.1747` n `237`; crypto_major avg `0.0377` n `8`; equity avg `-0.0752` n `151`; fx avg `0.0084` n `6`; index avg `-0.0094` n `26`; metal avg `-0.0133` n `20`; unknown avg `0.1488` n `1149`
- 4h: commodity avg `0.0579` n `13`; crypto_alt avg `0.0593` n `237`; crypto_major avg `-0.0931` n `8`; equity avg `-0.0772` n `151`; fx avg `-0.0335` n `6`; index avg `-0.0187` n `26`; metal avg `-0.1417` n `20`; unknown avg `0.4398` n `1126`
- 24h: commodity avg `-0.3929` n `13`; crypto_alt avg `0.6824` n `237`; crypto_major avg `1.3024` n `8`; equity avg `2.5044` n `151`; fx avg `-0.0461` n `6`; index avg `0.4465` n `26`; metal avg `0.2061` n `20`; unknown avg `1.5215` n `915`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1986`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1451`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1271`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0634`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
