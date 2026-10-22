# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T03:37:31.857623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.7` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.0235` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7135` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0119` n `13`; crypto_alt avg `-0.1992` n `237`; crypto_major avg `-0.1079` n `8`; equity avg `-0.2829` n `151`; fx avg `-0.008` n `6`; index avg `-0.0806` n `26`; metal avg `-0.0882` n `20`; unknown avg `2.4551` n `1199`
- 1h: commodity avg `-0.0136` n `13`; crypto_alt avg `-0.387` n `237`; crypto_major avg `-0.3081` n `8`; equity avg `-0.3223` n `151`; fx avg `-0.012` n `6`; index avg `-0.0718` n `26`; metal avg `-0.1725` n `20`; unknown avg `5.6204` n `1189`
- 4h: commodity avg `0.1242` n `13`; crypto_alt avg `-2.1207` n `237`; crypto_major avg `-1.8993` n `8`; equity avg `-1.3665` n `151`; fx avg `-0.0468` n `6`; index avg `-0.1858` n `26`; metal avg `-0.4842` n `20`; unknown avg `12.9179` n `1183`
- 24h: commodity avg `-0.6057` n `13`; crypto_alt avg `-0.753` n `237`; crypto_major avg `-0.7469` n `8`; equity avg `-2.0522` n `151`; fx avg `-0.0276` n `6`; index avg `-0.2857` n `26`; metal avg `-0.5551` n `20`; unknown avg `121.5277` n `936`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
