# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T12:37:35.127903+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0895` n `12`; crypto_alt avg `-0.1516` n `228`; crypto_major avg `0.0994` n `8`; equity avg `0.0275` n `74`; fx avg `0.0255` n `6`; index avg `0.0679` n `23`; metal avg `0.0311` n `18`; unknown avg `0.1319` n `644`
- 1h: commodity avg `-0.1658` n `12`; crypto_alt avg `0.0378` n `228`; crypto_major avg `0.2934` n `8`; equity avg `0.0399` n `74`; fx avg `0.0221` n `6`; index avg `0.0669` n `23`; metal avg `0.2286` n `18`; unknown avg `0.0923` n `644`
- 4h: commodity avg `-0.3354` n `12`; crypto_alt avg `0.4043` n `228`; crypto_major avg `0.3973` n `8`; equity avg `-0.0289` n `74`; fx avg `0.0334` n `6`; index avg `0.1306` n `23`; metal avg `0.0643` n `18`; unknown avg `0.5333` n `635`
- 24h: commodity avg `-0.7898` n `12`; crypto_alt avg `1.1152` n `228`; crypto_major avg `0.4254` n `8`; equity avg `-0.3616` n `74`; fx avg `0.0592` n `6`; index avg `0.8638` n `23`; metal avg `0.9344` n `18`; unknown avg `27.658` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
