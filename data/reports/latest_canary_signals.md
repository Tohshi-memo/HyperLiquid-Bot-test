# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T12:52:34.199767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0733` n `13`; crypto_alt avg `0.1725` n `239`; crypto_major avg `0.1443` n `8`; equity avg `0.124` n `157`; fx avg `-0.0085` n `6`; index avg `0.0171` n `27`; metal avg `0.1159` n `20`; unknown avg `0.0098` n `1262`
- 1h: commodity avg `-0.4083` n `13`; crypto_alt avg `0.8202` n `239`; crypto_major avg `0.8848` n `8`; equity avg `0.5972` n `157`; fx avg `-0.0129` n `6`; index avg `0.0831` n `27`; metal avg `0.2538` n `20`; unknown avg `0.3971` n `1250`
- 4h: commodity avg `-0.3121` n `13`; crypto_alt avg `2.1384` n `239`; crypto_major avg `1.5798` n `8`; equity avg `1.3942` n `157`; fx avg `0.0044` n `6`; index avg `0.133` n `27`; metal avg `0.3868` n `20`; unknown avg `215.9305` n `1214`
- 24h: commodity avg `-0.6097` n `13`; crypto_alt avg `-0.0779` n `238`; crypto_major avg `0.1724` n `8`; equity avg `-2.659` n `157`; fx avg `-0.0064` n `6`; index avg `-0.1489` n `27`; metal avg `-0.1299` n `20`; unknown avg `249.3382` n `1020`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
