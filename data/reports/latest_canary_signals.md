# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T05:52:30.658788+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0195` n `12`; crypto_alt avg `0.4469` n `234`; crypto_major avg `0.3322` n `8`; equity avg `-0.0312` n `141`; fx avg `0.0096` n `6`; index avg `-0.018` n `26`; metal avg `-0.0016` n `20`; unknown avg `5.9348` n `962`
- 1h: commodity avg `0.0152` n `12`; crypto_alt avg `-0.9788` n `234`; crypto_major avg `-0.7717` n `8`; equity avg `-0.2643` n `141`; fx avg `0.0342` n `6`; index avg `-0.0365` n `26`; metal avg `-0.1055` n `20`; unknown avg `31.3551` n `960`
- 4h: commodity avg `0.2213` n `12`; crypto_alt avg `-1.8105` n `234`; crypto_major avg `-1.0492` n `8`; equity avg `-0.5771` n `141`; fx avg `-0.0049` n `6`; index avg `-0.0685` n `26`; metal avg `-0.2448` n `20`; unknown avg `321.6692` n `946`
- 24h: commodity avg `-0.3132` n `12`; crypto_alt avg `-2.2642` n `234`; crypto_major avg `-2.1166` n `8`; equity avg `-1.66` n `141`; fx avg `0.0782` n `6`; index avg `-0.1756` n `26`; metal avg `-0.8039` n `20`; unknown avg `5.9194` n `811`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
