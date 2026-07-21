# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T20:52:28.887184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0438` n `12`; crypto_alt avg `-0.0199` n `230`; crypto_major avg `-0.0575` n `8`; equity avg `-0.0118` n `98`; fx avg `-0.0062` n `6`; index avg `-0.0081` n `25`; metal avg `-0.0314` n `20`; unknown avg `0.0478` n `771`
- 1h: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.0196` n `230`; crypto_major avg `-0.0677` n `8`; equity avg `0.3469` n `98`; fx avg `0.0039` n `6`; index avg `-0.022` n `25`; metal avg `-0.0387` n `20`; unknown avg `0.0943` n `771`
- 4h: commodity avg `0.0601` n `12`; crypto_alt avg `0.0267` n `230`; crypto_major avg `-0.3733` n `8`; equity avg `0.3487` n `98`; fx avg `0.0416` n `6`; index avg `-0.0305` n `25`; metal avg `-0.0321` n `20`; unknown avg `-0.1902` n `771`
- 24h: commodity avg `0.4827` n `12`; crypto_alt avg `0.7827` n `230`; crypto_major avg `0.5959` n `8`; equity avg `4.338` n `98`; fx avg `0.075` n `6`; index avg `0.628` n `25`; metal avg `0.7301` n `20`; unknown avg `0.3256` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0847`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
