# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T23:22:27.080314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.37` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1005` n `12`; crypto_alt avg `0.2155` n `230`; crypto_major avg `0.0382` n `8`; equity avg `0.3568` n `102`; fx avg `0.0036` n `6`; index avg `0.0517` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.0965` n `776`
- 1h: commodity avg `0.1818` n `12`; crypto_alt avg `-0.4603` n `230`; crypto_major avg `-0.7221` n `8`; equity avg `-0.8835` n `102`; fx avg `-0.0142` n `6`; index avg `-0.0912` n `25`; metal avg `-0.0312` n `20`; unknown avg `0.3599` n `776`
- 4h: commodity avg `0.6837` n `12`; crypto_alt avg `-0.2703` n `230`; crypto_major avg `-0.3361` n `8`; equity avg `-0.5022` n `102`; fx avg `-0.0239` n `6`; index avg `-0.1141` n `25`; metal avg `-0.0912` n `20`; unknown avg `0.3244` n `776`
- 24h: commodity avg `-0.2379` n `12`; crypto_alt avg `-0.7362` n `230`; crypto_major avg `-0.6024` n `8`; equity avg `-3.0501` n `102`; fx avg `-0.0981` n `6`; index avg `-0.4238` n `25`; metal avg `-0.4602` n `20`; unknown avg `0.2408` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
