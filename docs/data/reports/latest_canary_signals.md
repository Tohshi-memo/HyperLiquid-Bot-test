# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T15:52:28.662479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0306` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `1.0204` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0069` n `13`; crypto_alt avg `0.0058` n `237`; crypto_major avg `0.0176` n `8`; equity avg `0.0777` n `151`; fx avg `-0.0049` n `6`; index avg `0.0278` n `26`; metal avg `0.0407` n `20`; unknown avg `-0.0615` n `1199`
- 1h: commodity avg `0.1714` n `13`; crypto_alt avg `-1.2115` n `237`; crypto_major avg `-1.105` n `8`; equity avg `-0.5796` n `151`; fx avg `-0.0108` n `6`; index avg `-0.0846` n `26`; metal avg `-0.0773` n `20`; unknown avg `5.4923` n `1197`
- 4h: commodity avg `-0.7034` n `13`; crypto_alt avg `1.9841` n `237`; crypto_major avg `1.3272` n `8`; equity avg `1.9862` n `151`; fx avg `0.0481` n `6`; index avg `0.3315` n `26`; metal avg `0.2362` n `20`; unknown avg `2.7892` n `1100`
- 24h: commodity avg `-0.3428` n `13`; crypto_alt avg `1.8792` n `237`; crypto_major avg `0.9854` n `8`; equity avg `-0.9618` n `151`; fx avg `0.0232` n `6`; index avg `-0.1498` n `26`; metal avg `0.0514` n `20`; unknown avg `3.8631` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
