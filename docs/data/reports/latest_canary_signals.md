# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T02:22:33.043095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0451` n `12`; crypto_alt avg `-0.0839` n `230`; crypto_major avg `0.085` n `8`; equity avg `0.042` n `102`; fx avg `-0.0037` n `6`; index avg `-0.0542` n `25`; metal avg `0.1` n `20`; unknown avg `0.3895` n `777`
- 1h: commodity avg `-0.022` n `12`; crypto_alt avg `-0.6264` n `230`; crypto_major avg `-0.2751` n `8`; equity avg `-0.8933` n `102`; fx avg `-0.0151` n `6`; index avg `-0.2956` n `25`; metal avg `0.1215` n `20`; unknown avg `2.5354` n `777`
- 4h: commodity avg `0.2018` n `12`; crypto_alt avg `-1.0276` n `230`; crypto_major avg `-0.4475` n `8`; equity avg `-1.1669` n `102`; fx avg `-0.0173` n `6`; index avg `-0.3346` n `25`; metal avg `0.1033` n `20`; unknown avg `0.4475` n `776`
- 24h: commodity avg `-0.0414` n `12`; crypto_alt avg `-0.8154` n `230`; crypto_major avg `0.2836` n `8`; equity avg `-2.2419` n `102`; fx avg `-0.1321` n `6`; index avg `-0.4137` n `25`; metal avg `-0.0698` n `20`; unknown avg `0.0051` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
