# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T19:22:38.443269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `-0.0104` n `230`; crypto_major avg `-0.0271` n `8`; equity avg `0.2579` n `102`; fx avg `-0.0009` n `6`; index avg `0.0057` n `25`; metal avg `0.0034` n `20`; unknown avg `-0.0024` n `776`
- 1h: commodity avg `-0.0381` n `12`; crypto_alt avg `0.0895` n `230`; crypto_major avg `0.1495` n `8`; equity avg `0.597` n `102`; fx avg `0.0256` n `6`; index avg `0.0535` n `25`; metal avg `0.0132` n `20`; unknown avg `0.0021` n `775`
- 4h: commodity avg `-0.144` n `12`; crypto_alt avg `-0.2896` n `230`; crypto_major avg `-0.0802` n `8`; equity avg `0.5354` n `102`; fx avg `-0.0064` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0517` n `20`; unknown avg `-0.344` n `774`
- 24h: commodity avg `-0.9448` n `12`; crypto_alt avg `-2.0156` n `230`; crypto_major avg `-1.8364` n `8`; equity avg `-3.0422` n `102`; fx avg `-0.0885` n `6`; index avg `-0.365` n `25`; metal avg `-0.4655` n `20`; unknown avg `-0.4948` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
