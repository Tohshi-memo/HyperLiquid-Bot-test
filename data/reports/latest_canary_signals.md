# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T08:07:23.259004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `13`; crypto_alt avg `-0.1133` n `235`; crypto_major avg `-0.0101` n `8`; equity avg `-0.0085` n `150`; fx avg `0.0031` n `6`; index avg `-0.001` n `26`; metal avg `-0.0035` n `20`; unknown avg `-0.0929` n `1099`
- 1h: commodity avg `0.0071` n `13`; crypto_alt avg `-0.3044` n `235`; crypto_major avg `-0.1919` n `8`; equity avg `-0.0308` n `150`; fx avg `0.0038` n `6`; index avg `-0.0021` n `26`; metal avg `0.0031` n `20`; unknown avg `0.1047` n `1099`
- 4h: commodity avg `0.0286` n `13`; crypto_alt avg `0.9903` n `235`; crypto_major avg `0.155` n `8`; equity avg `0.0505` n `150`; fx avg `0.0055` n `6`; index avg `0.0125` n `26`; metal avg `0.0145` n `20`; unknown avg `0.3445` n `1083`
- 24h: commodity avg `0.1702` n `13`; crypto_alt avg `0.8861` n `235`; crypto_major avg `-0.3248` n `8`; equity avg `0.0424` n `150`; fx avg `-0.0227` n `6`; index avg `0.0014` n `26`; metal avg `0.0023` n `20`; unknown avg `0.3596` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
