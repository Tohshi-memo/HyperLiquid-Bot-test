# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T15:37:30.289121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.019` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `1.3179` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0862` n `13`; crypto_alt avg `-0.0277` n `237`; crypto_major avg `0.0478` n `8`; equity avg `-0.147` n `151`; fx avg `-0.0124` n `6`; index avg `-0.0346` n `26`; metal avg `-0.022` n `20`; unknown avg `0.1569` n `1199`
- 1h: commodity avg `0.1642` n `13`; crypto_alt avg `-1.5686` n `237`; crypto_major avg `-1.4244` n `8`; equity avg `-0.667` n `151`; fx avg `-0.0134` n `6`; index avg `-0.1065` n `26`; metal avg `-0.1717` n `20`; unknown avg `6.6623` n `1197`
- 4h: commodity avg `-0.7533` n `13`; crypto_alt avg `1.9057` n `237`; crypto_major avg `1.2657` n `8`; equity avg `1.868` n `151`; fx avg `0.0547` n `6`; index avg `0.2909` n `26`; metal avg `0.1547` n `20`; unknown avg `3.1207` n `1100`
- 24h: commodity avg `-0.2713` n `13`; crypto_alt avg `1.7233` n `237`; crypto_major avg `0.8157` n `8`; equity avg `-1.0637` n `151`; fx avg `0.0115` n `6`; index avg `-0.1797` n `26`; metal avg `-0.0078` n `20`; unknown avg `3.9797` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
