# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T17:52:37.611732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.19` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0736` n `12`; crypto_alt avg `-0.0618` n `229`; crypto_major avg `0.0097` n `8`; equity avg `-0.0079` n `91`; fx avg `-0.0032` n `6`; index avg `0.013` n `25`; metal avg `-0.0132` n `20`; unknown avg `0.7885` n `763`
- 1h: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.391` n `229`; crypto_major avg `-0.1098` n `8`; equity avg `0.0516` n `91`; fx avg `0.0029` n `6`; index avg `0.0473` n `25`; metal avg `-0.0033` n `20`; unknown avg `-0.0451` n `763`
- 4h: commodity avg `0.1929` n `12`; crypto_alt avg `0.2065` n `229`; crypto_major avg `0.9918` n `8`; equity avg `-0.0725` n `91`; fx avg `-0.0421` n `6`; index avg `0.0293` n `25`; metal avg `-0.2009` n `20`; unknown avg `0.1915` n `755`
- 24h: commodity avg `0.5723` n `12`; crypto_alt avg `-0.8354` n `229`; crypto_major avg `0.101` n `8`; equity avg `-2.4872` n `91`; fx avg `-0.2429` n `6`; index avg `-0.4421` n `25`; metal avg `-0.1521` n `20`; unknown avg `-0.0436` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
