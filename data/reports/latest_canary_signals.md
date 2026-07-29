# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T00:52:28.419065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.23` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `0.0559` n `230`; crypto_major avg `0.0869` n `8`; equity avg `-0.035` n `102`; fx avg `-0.0065` n `6`; index avg `0.0186` n `25`; metal avg `-0.0239` n `20`; unknown avg `-0.1418` n `777`
- 1h: commodity avg `0.0523` n `12`; crypto_alt avg `0.1065` n `230`; crypto_major avg `0.271` n `8`; equity avg `0.194` n `102`; fx avg `0.0091` n `6`; index avg `0.0208` n `25`; metal avg `0.0207` n `20`; unknown avg `-0.1409` n `777`
- 4h: commodity avg `0.7218` n `12`; crypto_alt avg `0.0541` n `230`; crypto_major avg `0.2023` n `8`; equity avg `0.4537` n `102`; fx avg `0.026` n `6`; index avg `0.1454` n `25`; metal avg `0.0298` n `20`; unknown avg `-0.1872` n `776`
- 24h: commodity avg `-0.2279` n `12`; crypto_alt avg `0.1196` n `230`; crypto_major avg `0.6794` n `8`; equity avg `-1.2007` n `102`; fx avg `-0.1313` n `6`; index avg `0.0027` n `25`; metal avg `-0.2217` n `20`; unknown avg `0.3318` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
