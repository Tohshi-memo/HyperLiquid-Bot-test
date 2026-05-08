# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T07:07:11.682431+00:00`
- Correlation status: `ready`
- Asset price records: `624`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.03` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0699` n `12`; crypto_alt avg `-0.2802` n `228`; crypto_major avg `-0.1881` n `8`; equity avg `-0.0172` n `65`; fx avg `0.0024` n `5`; index avg `-0.0377` n `23`; metal avg `-0.1262` n `18`; unknown avg `0.7672` n `375`
- 1h: commodity avg `-0.0231` n `12`; crypto_alt avg `-0.1256` n `228`; crypto_major avg `-0.1797` n `8`; equity avg `0.1688` n `65`; fx avg `0.0151` n `5`; index avg `0.0327` n `23`; metal avg `-0.2385` n `18`; unknown avg `0.6426` n `375`
- 4h: commodity avg `-0.2674` n `12`; crypto_alt avg `0.217` n `228`; crypto_major avg `-0.0777` n `8`; equity avg `0.4628` n `65`; fx avg `0.1065` n `5`; index avg `0.162` n `23`; metal avg `0.5414` n `18`; unknown avg `0.0295` n `355`
- 24h: commodity avg `0.9894` n `12`; crypto_alt avg `0.0969` n `228`; crypto_major avg `-2.365` n `8`; equity avg `-1.1175` n `65`; fx avg `0.3416` n `5`; index avg `-0.6694` n `23`; metal avg `-0.0371` n `18`; unknown avg `0.6018` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1348`, n `616`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1338`, n `616`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `620`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1154`, n `620`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1117`, n `620`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `620`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `616`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.082`, n `616`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.081`, n `616`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0668`, n `620`, weak_sample_signal
