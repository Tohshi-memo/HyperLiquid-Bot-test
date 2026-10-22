# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T05:08:08.430538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.78` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.1698` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0952` n `13`; crypto_alt avg `-0.0025` n `237`; crypto_major avg `-0.0092` n `8`; equity avg `0.0027` n `151`; fx avg `0.0074` n `6`; index avg `-0.0043` n `26`; metal avg `0.0008` n `20`; unknown avg `3.6182` n `1199`
- 1h: commodity avg `0.1223` n `13`; crypto_alt avg `-0.2749` n `237`; crypto_major avg `-0.0775` n `8`; equity avg `-0.0398` n `151`; fx avg `0.0063` n `6`; index avg `-0.0333` n `26`; metal avg `-0.0033` n `20`; unknown avg `4.0999` n `1199`
- 4h: commodity avg `0.2023` n `13`; crypto_alt avg `-2.0573` n `237`; crypto_major avg `-1.4132` n `8`; equity avg `-1.4286` n `151`; fx avg `-0.0514` n `6`; index avg `-0.2434` n `26`; metal avg `-0.3139` n `20`; unknown avg `2.5195` n `1177`
- 24h: commodity avg `-0.344` n `13`; crypto_alt avg `-0.756` n `237`; crypto_major avg `-0.6024` n `8`; equity avg `-2.0131` n `151`; fx avg `-0.0066` n `6`; index avg `-0.3058` n `26`; metal avg `-0.5336` n `20`; unknown avg `118.6639` n `930`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
