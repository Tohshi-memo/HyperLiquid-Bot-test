# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T11:07:32.165952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0445` n `13`; crypto_alt avg `-0.0497` n `235`; crypto_major avg `-0.1194` n `8`; equity avg `-0.0385` n `150`; fx avg `0.0043` n `6`; index avg `0.0004` n `26`; metal avg `-0.049` n `20`; unknown avg `0.282` n `1072`
- 1h: commodity avg `-0.0493` n `13`; crypto_alt avg `0.3627` n `235`; crypto_major avg `0.2282` n `8`; equity avg `0.0992` n `150`; fx avg `0.0014` n `6`; index avg `0.036` n `26`; metal avg `-0.0182` n `20`; unknown avg `1.1581` n `1072`
- 4h: commodity avg `-0.2954` n `13`; crypto_alt avg `0.8746` n `235`; crypto_major avg `0.5916` n `8`; equity avg `0.3183` n `149`; fx avg `0.0497` n `6`; index avg `0.0815` n `26`; metal avg `0.0741` n `20`; unknown avg `2.0368` n `1048`
- 24h: commodity avg `-0.7134` n `13`; crypto_alt avg `-0.3257` n `235`; crypto_major avg `-0.2031` n `8`; equity avg `0.7133` n `149`; fx avg `0.0679` n `6`; index avg `0.2397` n `26`; metal avg `-0.1734` n `20`; unknown avg `1.3071` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.182`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
