# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T01:07:25.202015+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `13`; crypto_alt avg `-0.1987` n `238`; crypto_major avg `-0.2637` n `8`; equity avg `-0.1379` n `155`; fx avg `-0.0093` n `6`; index avg `-0.013` n `27`; metal avg `0.088` n `20`; unknown avg `-0.0612` n `1232`
- 1h: commodity avg `0.0084` n `13`; crypto_alt avg `-0.5396` n `238`; crypto_major avg `-0.5762` n `8`; equity avg `0.0019` n `155`; fx avg `-0.0826` n `6`; index avg `0.0155` n `27`; metal avg `-0.0073` n `20`; unknown avg `-0.0331` n `1232`
- 4h: commodity avg `-0.0234` n `13`; crypto_alt avg `-0.912` n `238`; crypto_major avg `-0.7079` n `8`; equity avg `-0.1499` n `155`; fx avg `-0.1186` n `6`; index avg `0.0238` n `27`; metal avg `-0.0412` n `20`; unknown avg `3.0816` n `1150`
- 24h: commodity avg `-0.0571` n `13`; crypto_alt avg `0.0893` n `238`; crypto_major avg `0.0453` n `8`; equity avg `0.498` n `154`; fx avg `0.0697` n `6`; index avg `0.0966` n `27`; metal avg `-0.114` n `20`; unknown avg `24.5528` n `996`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
