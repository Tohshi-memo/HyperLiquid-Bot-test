# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T01:37:30.695971+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0297` n `13`; crypto_alt avg `-0.3923` n `238`; crypto_major avg `-0.2733` n `8`; equity avg `-0.2081` n `155`; fx avg `-0.0234` n `6`; index avg `-0.0448` n `27`; metal avg `-0.0901` n `20`; unknown avg `1.7567` n `1238`
- 1h: commodity avg `0.0742` n `13`; crypto_alt avg `-0.8503` n `238`; crypto_major avg `-0.688` n `8`; equity avg `-0.6802` n `155`; fx avg `-0.0248` n `6`; index avg `-0.132` n `27`; metal avg `0.0553` n `20`; unknown avg `0.3803` n `1232`
- 4h: commodity avg `0.0455` n `13`; crypto_alt avg `-1.1473` n `238`; crypto_major avg `-0.8492` n `8`; equity avg `-0.3669` n `155`; fx avg `-0.1318` n `6`; index avg `-0.0673` n `27`; metal avg `-0.0475` n `20`; unknown avg `1.9095` n `1150`
- 24h: commodity avg `0.0368` n `13`; crypto_alt avg `-0.7457` n `238`; crypto_major avg `-0.6359` n `8`; equity avg `-0.3028` n `154`; fx avg `-0.0007` n `6`; index avg `-0.0762` n `27`; metal avg `-0.1507` n `20`; unknown avg `27.1097` n `996`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
