# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T15:23:18.192154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0482` n `12`; crypto_alt avg `-0.0757` n `231`; crypto_major avg `-0.0168` n `8`; equity avg `0.1048` n `122`; fx avg `0.0024` n `6`; index avg `0.024` n `25`; metal avg `0.062` n `20`; unknown avg `-0.0362` n `795`
- 1h: commodity avg `-0.0126` n `12`; crypto_alt avg `0.1554` n `231`; crypto_major avg `0.2384` n `8`; equity avg `0.4986` n `122`; fx avg `-0.0095` n `6`; index avg `0.022` n `25`; metal avg `0.1437` n `20`; unknown avg `0.1151` n `795`
- 4h: commodity avg `-0.1499` n `12`; crypto_alt avg `-0.6872` n `231`; crypto_major avg `-0.3261` n `8`; equity avg `0.2791` n `122`; fx avg `0.0227` n `6`; index avg `-0.0653` n `25`; metal avg `0.0855` n `20`; unknown avg `-0.1008` n `795`
- 24h: commodity avg `-0.7004` n `12`; crypto_alt avg `-2.144` n `231`; crypto_major avg `-1.266` n `8`; equity avg `1.926` n `122`; fx avg `0.0224` n `6`; index avg `0.2615` n `25`; metal avg `-0.3606` n `20`; unknown avg `-1.0646` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
