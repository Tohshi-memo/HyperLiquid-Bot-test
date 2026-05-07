# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T11:37:16.622565+00:00`
- Correlation status: `ready`
- Asset price records: `546`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0597` n `12`; crypto_alt avg `-0.0188` n `228`; crypto_major avg `-0.0088` n `8`; equity avg `0.0857` n `65`; fx avg `-0.0117` n `4`; index avg `-0.0131` n `23`; metal avg `0.2366` n `18`; unknown avg `-0.1955` n `366`
- 1h: commodity avg `-0.6749` n `12`; crypto_alt avg `0.4472` n `228`; crypto_major avg `0.306` n `8`; equity avg `0.1228` n `65`; fx avg `-0.0219` n `4`; index avg `0.0021` n `23`; metal avg `0.2038` n `18`; unknown avg `0.1715` n `366`
- 4h: commodity avg `-0.295` n `12`; crypto_alt avg `-0.1105` n `228`; crypto_major avg `-0.5845` n `8`; equity avg `-0.1708` n `65`; fx avg `0.0661` n `4`; index avg `-0.1834` n `23`; metal avg `0.3055` n `18`; unknown avg `0.1579` n `358`
- 24h: commodity avg `0.3378` n `7`; crypto_alt avg `-0.0994` n `223`; crypto_major avg `-2.5785` n `7`; equity avg `-0.2258` n `47`; fx avg `0.1724` n `4`; index avg `0.0038` n `6`; metal avg `0.9869` n `7`; unknown avg `0.6239` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1312`, n `542`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1234`, n `542`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0931`, n `542`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0808`, n `538`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `538`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0774`, n `538`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0743`, n `538`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0711`, n `538`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `542`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0693`, n `538`, weak_sample_signal
