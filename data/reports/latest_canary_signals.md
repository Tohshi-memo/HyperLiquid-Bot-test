# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T11:07:24.106427+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.5` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0018` n `13`; crypto_alt avg `-0.0481` n `239`; crypto_major avg `0.0003` n `8`; equity avg `-0.0253` n `168`; fx avg `0.0016` n `6`; index avg `-0.0044` n `27`; metal avg `0.0081` n `20`; unknown avg `-0.0603` n `1255`
- 1h: commodity avg `-0.0059` n `13`; crypto_alt avg `-0.1803` n `239`; crypto_major avg `-0.3924` n `8`; equity avg `-0.1746` n `168`; fx avg `0.0044` n `6`; index avg `-0.0203` n `27`; metal avg `0.0008` n `20`; unknown avg `0.6635` n `1261`
- 4h: commodity avg `-0.025` n `13`; crypto_alt avg `-0.36` n `239`; crypto_major avg `-0.5217` n `8`; equity avg `-0.048` n `168`; fx avg `-0.012` n `6`; index avg `-0.012` n `27`; metal avg `0.0318` n `20`; unknown avg `2.8285` n `1211`
- 24h: commodity avg `-0.5573` n `13`; crypto_alt avg `-3.3802` n `239`; crypto_major avg `-3.3713` n `8`; equity avg `-0.5079` n `168`; fx avg `-0.0909` n `6`; index avg `0.0022` n `27`; metal avg `-0.2607` n `20`; unknown avg `191.2448` n `1085`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
