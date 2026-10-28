# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T19:07:32.019409+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.6` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0103` n `13`; crypto_alt avg `0.2122` n `238`; crypto_major avg `0.1607` n `8`; equity avg `0.051` n `155`; fx avg `-0.007` n `6`; index avg `-0.0193` n `27`; metal avg `0.0212` n `20`; unknown avg `0.4288` n `1230`
- 1h: commodity avg `-0.1351` n `13`; crypto_alt avg `0.6724` n `238`; crypto_major avg `0.4688` n `8`; equity avg `0.6309` n `155`; fx avg `-0.0085` n `6`; index avg `0.0298` n `27`; metal avg `0.0498` n `20`; unknown avg `0.8464` n `1232`
- 4h: commodity avg `-0.1413` n `13`; crypto_alt avg `0.6334` n `238`; crypto_major avg `0.7147` n `8`; equity avg `0.6391` n `155`; fx avg `0.0162` n `6`; index avg `0.0167` n `27`; metal avg `-0.0133` n `20`; unknown avg `1.8919` n `1226`
- 24h: commodity avg `0.5212` n `13`; crypto_alt avg `0.3028` n `238`; crypto_major avg `0.4004` n `8`; equity avg `1.4726` n `154`; fx avg `0.2405` n `6`; index avg `0.2435` n `27`; metal avg `-0.1469` n `20`; unknown avg `4.2469` n `1098`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
