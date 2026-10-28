# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T18:53:03.021508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.67` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0318` n `13`; crypto_alt avg `-0.2425` n `238`; crypto_major avg `-0.2384` n `8`; equity avg `-0.3103` n `155`; fx avg `-0.0183` n `6`; index avg `-0.0783` n `27`; metal avg `-0.1591` n `20`; unknown avg `2.4708` n `1232`
- 1h: commodity avg `-0.0648` n `13`; crypto_alt avg `0.4589` n `238`; crypto_major avg `0.2153` n `8`; equity avg `0.3744` n `155`; fx avg `0.0015` n `6`; index avg `0.0123` n `27`; metal avg `0.0074` n `20`; unknown avg `0.4621` n `1228`
- 4h: commodity avg `-0.1112` n `13`; crypto_alt avg `0.6375` n `238`; crypto_major avg `0.672` n `8`; equity avg `0.8561` n `155`; fx avg `0.0403` n `6`; index avg `0.0709` n `27`; metal avg `0.0055` n `20`; unknown avg `1.9962` n `1222`
- 24h: commodity avg `0.48` n `13`; crypto_alt avg `0.1527` n `238`; crypto_major avg `0.3712` n `8`; equity avg `1.5677` n `154`; fx avg `0.2521` n `6`; index avg `0.2916` n `27`; metal avg `-0.1219` n `20`; unknown avg `4.3539` n `1100`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
