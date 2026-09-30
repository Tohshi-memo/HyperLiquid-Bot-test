# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T15:52:34.310831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.34` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0582` n `12`; crypto_alt avg `0.2493` n `234`; crypto_major avg `0.3432` n `8`; equity avg `-0.0059` n `142`; fx avg `-0.0109` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0168` n `20`; unknown avg `0.5975` n `969`
- 1h: commodity avg `0.0811` n `12`; crypto_alt avg `0.3437` n `234`; crypto_major avg `0.6349` n `8`; equity avg `-0.095` n `142`; fx avg `0.0311` n `6`; index avg `-0.0338` n `26`; metal avg `-0.0949` n `20`; unknown avg `-0.042` n `909`
- 4h: commodity avg `0.1297` n `12`; crypto_alt avg `0.0242` n `234`; crypto_major avg `0.0276` n `8`; equity avg `0.1329` n `142`; fx avg `-0.0111` n `6`; index avg `0.1447` n `26`; metal avg `-0.157` n `20`; unknown avg `5.2659` n `875`
- 24h: commodity avg `0.1953` n `12`; crypto_alt avg `0.9682` n `234`; crypto_major avg `1.0141` n `8`; equity avg `-0.083` n `142`; fx avg `0.0557` n `6`; index avg `0.1716` n `26`; metal avg `-0.0233` n `20`; unknown avg `12.9075` n `820`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
