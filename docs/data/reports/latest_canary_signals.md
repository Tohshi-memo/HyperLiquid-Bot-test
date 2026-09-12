# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T17:17:19.921868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `12`; crypto_alt avg `-0.016` n `233`; crypto_major avg `-0.0435` n `8`; equity avg `-0.0158` n `136`; fx avg `0.0005` n `6`; index avg `-0.0003` n `26`; metal avg `0.0035` n `20`; unknown avg `0.004` n `838`
- 1h: commodity avg `0.0298` n `12`; crypto_alt avg `-0.119` n `233`; crypto_major avg `-0.0497` n `8`; equity avg `-0.0155` n `136`; fx avg `0.0026` n `6`; index avg `-0.0065` n `26`; metal avg `0.0103` n `20`; unknown avg `0.4079` n `790`
- 4h: commodity avg `0.0085` n `12`; crypto_alt avg `0.3466` n `233`; crypto_major avg `-0.0373` n `8`; equity avg `0.0345` n `136`; fx avg `-0.0063` n `6`; index avg `0.0078` n `26`; metal avg `0.026` n `20`; unknown avg `0.2015` n `790`
- 24h: commodity avg `-0.0783` n `12`; crypto_alt avg `0.5092` n `233`; crypto_major avg `-0.5312` n `8`; equity avg `-0.3389` n `136`; fx avg `-0.0128` n `6`; index avg `-0.0109` n `26`; metal avg `-0.0638` n `20`; unknown avg `1.0427` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0456`, n `668`, weak_sample_signal
