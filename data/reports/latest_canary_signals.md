# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T02:52:25.258941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.27` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0231` n `12`; crypto_alt avg `-0.2595` n `230`; crypto_major avg `-0.1984` n `8`; equity avg `-0.2411` n `102`; fx avg `-0.0023` n `6`; index avg `-0.0441` n `25`; metal avg `-0.0428` n `20`; unknown avg `-0.009` n `777`
- 1h: commodity avg `-0.1422` n `12`; crypto_alt avg `-0.1256` n `230`; crypto_major avg `0.2426` n `8`; equity avg `-0.1338` n `102`; fx avg `-0.0304` n `6`; index avg `-0.1567` n `25`; metal avg `0.1063` n `20`; unknown avg `0.5281` n `777`
- 4h: commodity avg `-0.0497` n `12`; crypto_alt avg `-0.4815` n `230`; crypto_major avg `0.2251` n `8`; equity avg `-0.3194` n `102`; fx avg `-0.0231` n `6`; index avg `-0.2708` n `25`; metal avg `0.1263` n `20`; unknown avg `0.2158` n `776`
- 24h: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.6499` n `230`; crypto_major avg `0.7046` n `8`; equity avg `-1.9635` n `102`; fx avg `-0.0946` n `6`; index avg `-0.3927` n `25`; metal avg `-0.0304` n `20`; unknown avg `0.0645` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
