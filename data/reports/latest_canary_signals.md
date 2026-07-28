# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T23:52:30.570553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.36` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.093` n `12`; crypto_alt avg `0.2104` n `230`; crypto_major avg `0.3076` n `8`; equity avg `0.8033` n `102`; fx avg `0.007` n `6`; index avg `0.1392` n `25`; metal avg `0.056` n `20`; unknown avg `0.1141` n `777`
- 1h: commodity avg `-0.0335` n `12`; crypto_alt avg `0.362` n `230`; crypto_major avg `0.2893` n `8`; equity avg `1.1831` n `102`; fx avg `-0.0012` n `6`; index avg `0.2372` n `25`; metal avg `0.084` n `20`; unknown avg `0.0849` n `776`
- 4h: commodity avg `0.6529` n `12`; crypto_alt avg `0.0015` n `230`; crypto_major avg `-0.0133` n `8`; equity avg `0.7597` n `102`; fx avg `-0.0123` n `6`; index avg `0.1314` n `25`; metal avg `-0.0197` n `20`; unknown avg `0.3871` n `776`
- 24h: commodity avg `-0.3128` n `12`; crypto_alt avg `0.0406` n `230`; crypto_major avg `0.1957` n `8`; equity avg `-2.0049` n `102`; fx avg `-0.0879` n `6`; index avg `-0.2048` n `25`; metal avg `-0.3837` n `20`; unknown avg `0.401` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
