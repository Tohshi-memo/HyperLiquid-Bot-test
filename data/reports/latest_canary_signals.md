# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T03:52:27.120485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.63` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.5969` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0313` n `13`; crypto_alt avg `0.1198` n `237`; crypto_major avg `0.1111` n `8`; equity avg `-0.0312` n `151`; fx avg `-0.0031` n `6`; index avg `-0.0081` n `26`; metal avg `-0.0105` n `20`; unknown avg `3.0452` n `1197`
- 1h: commodity avg `0.0321` n `13`; crypto_alt avg `-0.2379` n `237`; crypto_major avg `-0.0759` n `8`; equity avg `-0.275` n `151`; fx avg `-0.0105` n `6`; index avg `-0.0838` n `26`; metal avg `-0.1306` n `20`; unknown avg `-0.1181` n `1187`
- 4h: commodity avg `0.1553` n `13`; crypto_alt avg `-2.0049` n `237`; crypto_major avg `-1.7907` n `8`; equity avg `-1.3974` n `151`; fx avg `-0.05` n `6`; index avg `-0.1938` n `26`; metal avg `-0.4945` n `20`; unknown avg `5.5891` n `1179`
- 24h: commodity avg `-0.5426` n `13`; crypto_alt avg `-0.6627` n `237`; crypto_major avg `-0.5916` n `8`; equity avg `-2.0437` n `151`; fx avg `-0.0199` n `6`; index avg `-0.2924` n `26`; metal avg `-0.5534` n `20`; unknown avg `118.4895` n `932`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
