# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T04:07:29.039123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.63` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.5015` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0017` n `13`; crypto_alt avg `0.0877` n `237`; crypto_major avg `0.078` n `8`; equity avg `-0.0577` n `151`; fx avg `-0.0094` n `6`; index avg `-0.0193` n `26`; metal avg `0.0` n `20`; unknown avg `0.3584` n `1189`
- 1h: commodity avg `0.011` n `13`; crypto_alt avg `-0.1776` n `237`; crypto_major avg `-0.0192` n `8`; equity avg `-0.3289` n `151`; fx avg `-0.0261` n `6`; index avg `-0.0885` n `26`; metal avg `-0.1273` n `20`; unknown avg `-0.3126` n `1179`
- 4h: commodity avg `0.157` n `13`; crypto_alt avg `-1.9204` n `237`; crypto_major avg `-1.7144` n `8`; equity avg `-1.4538` n `151`; fx avg `-0.0595` n `6`; index avg `-0.2129` n `26`; metal avg `-0.4946` n `20`; unknown avg `6.9835` n `1177`
- 24h: commodity avg `-0.5748` n `13`; crypto_alt avg `-0.4891` n `237`; crypto_major avg `-0.3987` n `8`; equity avg `-1.9633` n `151`; fx avg `-0.0223` n `6`; index avg `-0.2814` n `26`; metal avg `-0.5227` n `20`; unknown avg `118.8871` n `930`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
