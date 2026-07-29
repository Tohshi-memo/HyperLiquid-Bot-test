# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T20:07:35.433936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.49` - Polymarket crypto volume is unusually high.
- 1h_crypto_equity_divergence: score `1.5927` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.021` n `12`; crypto_alt avg `-0.1562` n `230`; crypto_major avg `-0.029` n `8`; equity avg `-0.3642` n `102`; fx avg `0.0104` n `6`; index avg `-0.1628` n `25`; metal avg `-0.1505` n `20`; unknown avg `0.1029` n `778`
- 1h: commodity avg `0.0704` n `12`; crypto_alt avg `-1.3454` n `230`; crypto_major avg `-1.2334` n `8`; equity avg `-2.8261` n `102`; fx avg `0.0419` n `6`; index avg `-0.6821` n `25`; metal avg `-0.4584` n `20`; unknown avg `-0.3259` n `778`
- 4h: commodity avg `-0.0087` n `12`; crypto_alt avg `-0.4295` n `230`; crypto_major avg `-0.509` n `8`; equity avg `-0.4343` n `102`; fx avg `0.1059` n `6`; index avg `-0.2125` n `25`; metal avg `0.3058` n `20`; unknown avg `-0.4721` n `778`
- 24h: commodity avg `1.3394` n `12`; crypto_alt avg `-2.8412` n `230`; crypto_major avg `-1.1047` n `8`; equity avg `-3.1754` n `102`; fx avg `0.0204` n `6`; index avg `-0.7018` n `25`; metal avg `0.0898` n `20`; unknown avg `-0.7545` n `760`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
