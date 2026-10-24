# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T13:37:27.492731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.055` n `13`; crypto_alt avg `-0.2759` n `237`; crypto_major avg `-0.08` n `8`; equity avg `-0.0247` n `152`; fx avg `-0.002` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0042` n `20`; unknown avg `-0.1304` n `1200`
- 1h: commodity avg `-0.0174` n `13`; crypto_alt avg `-0.4789` n `237`; crypto_major avg `-0.1815` n `8`; equity avg `-0.1072` n `152`; fx avg `-0.005` n `6`; index avg `-0.0149` n `26`; metal avg `-0.002` n `20`; unknown avg `-0.068` n `1198`
- 4h: commodity avg `0.0998` n `13`; crypto_alt avg `-0.2861` n `237`; crypto_major avg `0.2644` n `8`; equity avg `0.1229` n `152`; fx avg `-0.0085` n `6`; index avg `0.0013` n `26`; metal avg `0.0142` n `20`; unknown avg `0.6716` n `1190`
- 24h: commodity avg `0.4436` n `13`; crypto_alt avg `-2.7422` n `237`; crypto_major avg `-1.9998` n `8`; equity avg `0.4407` n `152`; fx avg `0.0085` n `6`; index avg `0.071` n `26`; metal avg `-0.1679` n `20`; unknown avg `194.6622` n `1051`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1927`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1926`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
