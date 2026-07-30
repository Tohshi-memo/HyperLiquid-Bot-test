# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T22:22:37.569532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0327` n `12`; crypto_alt avg `-0.0784` n `230`; crypto_major avg `0.031` n `8`; equity avg `0.0715` n `102`; fx avg `0.0144` n `6`; index avg `0.031` n `25`; metal avg `0.0125` n `20`; unknown avg `-0.0804` n `779`
- 1h: commodity avg `0.0439` n `12`; crypto_alt avg `0.0528` n `230`; crypto_major avg `0.2123` n `8`; equity avg `0.2699` n `102`; fx avg `0.034` n `6`; index avg `0.0553` n `25`; metal avg `0.0177` n `20`; unknown avg `0.1437` n `779`
- 4h: commodity avg `0.0339` n `12`; crypto_alt avg `0.0604` n `230`; crypto_major avg `0.1541` n `8`; equity avg `1.4909` n `102`; fx avg `0.0629` n `6`; index avg `0.1574` n `25`; metal avg `0.107` n `20`; unknown avg `-0.1868` n `779`
- 24h: commodity avg `0.0232` n `12`; crypto_alt avg `0.8755` n `230`; crypto_major avg `1.6165` n `8`; equity avg `7.5626` n `102`; fx avg `-0.3975` n `6`; index avg `0.9224` n `25`; metal avg `0.5874` n `20`; unknown avg `0.0797` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
