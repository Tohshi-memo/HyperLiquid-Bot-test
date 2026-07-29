# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T01:52:29.301355+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0424` n `12`; crypto_alt avg `-0.3095` n `230`; crypto_major avg `-0.2849` n `8`; equity avg `-0.8821` n `102`; fx avg `-0.0067` n `6`; index avg `-0.2026` n `25`; metal avg `-0.1219` n `20`; unknown avg `0.5651` n `777`
- 1h: commodity avg `0.0744` n `12`; crypto_alt avg `-0.7933` n `230`; crypto_major avg `-0.5758` n `8`; equity avg `-1.5131` n `102`; fx avg `-0.0006` n `6`; index avg `-0.369` n `25`; metal avg `-0.0843` n `20`; unknown avg `0.7237` n `777`
- 4h: commodity avg `0.5026` n `12`; crypto_alt avg `-0.9298` n `230`; crypto_major avg `-0.6495` n `8`; equity avg `-1.2469` n `102`; fx avg `-0.0025` n `6`; index avg `-0.2821` n `25`; metal avg `-0.0871` n `20`; unknown avg `0.4729` n `776`
- 24h: commodity avg `-0.0944` n `12`; crypto_alt avg `-0.2151` n `230`; crypto_major avg `0.3969` n `8`; equity avg `-2.1312` n `102`; fx avg `-0.1403` n `6`; index avg `-0.2951` n `25`; metal avg `-0.137` n `20`; unknown avg `-0.0585` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
