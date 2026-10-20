# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T15:22:37.256755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0037` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `1.0002` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.009` n `13`; crypto_alt avg `-1.1655` n `237`; crypto_major avg `-1.2275` n `8`; equity avg `-0.4272` n `151`; fx avg `0.0036` n `6`; index avg `-0.0801` n `26`; metal avg `-0.0804` n `20`; unknown avg `2.9453` n `1199`
- 1h: commodity avg `-0.0998` n `13`; crypto_alt avg `-0.7394` n `237`; crypto_major avg `-0.9828` n `8`; equity avg `0.1315` n `151`; fx avg `-0.0135` n `6`; index avg `0.0174` n `26`; metal avg `-0.0379` n `20`; unknown avg `0.7187` n `1197`
- 4h: commodity avg `-0.759` n `13`; crypto_alt avg `1.9827` n `237`; crypto_major avg `1.2447` n `8`; equity avg `1.9494` n `151`; fx avg `0.0682` n `6`; index avg `0.3052` n `26`; metal avg `0.1685` n `20`; unknown avg `2.6365` n `1100`
- 24h: commodity avg `-0.3553` n `13`; crypto_alt avg `1.3987` n `237`; crypto_major avg `0.3698` n `8`; equity avg `-0.7116` n `151`; fx avg `0.0291` n `6`; index avg `-0.1058` n `26`; metal avg `0.0657` n `20`; unknown avg `3.8853` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
