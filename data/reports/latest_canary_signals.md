# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T18:52:28.826661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `13`; crypto_alt avg `0.0444` n `235`; crypto_major avg `0.0373` n `8`; equity avg `0.009` n `150`; fx avg `-0.0014` n `6`; index avg `0.0014` n `26`; metal avg `-0.0034` n `20`; unknown avg `26.3365` n `1077`
- 1h: commodity avg `0.0013` n `13`; crypto_alt avg `0.1996` n `235`; crypto_major avg `0.0132` n `8`; equity avg `0.003` n `150`; fx avg `0.0011` n `6`; index avg `-0.0055` n `26`; metal avg `-0.0019` n `20`; unknown avg `5.219` n `1067`
- 4h: commodity avg `-0.0263` n `13`; crypto_alt avg `0.2003` n `235`; crypto_major avg `-0.2431` n `8`; equity avg `-0.0443` n `150`; fx avg `-0.005` n `6`; index avg `-0.0217` n `26`; metal avg `-0.0273` n `20`; unknown avg `2.9396` n `1031`
- 24h: commodity avg `-0.178` n `13`; crypto_alt avg `2.7613` n `235`; crypto_major avg `0.9496` n `8`; equity avg `0.1019` n `150`; fx avg `-0.0077` n `6`; index avg `-0.0091` n `26`; metal avg `-0.0614` n `20`; unknown avg `3.972` n `944`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
