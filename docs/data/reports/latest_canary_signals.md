# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T04:22:28.150829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6352` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0382` n `12`; crypto_alt avg `0.5819` n `234`; crypto_major avg `0.3192` n `8`; equity avg `0.1735` n `141`; fx avg `-0.0038` n `6`; index avg `0.0366` n `26`; metal avg `0.0138` n `20`; unknown avg `0.5808` n `962`
- 1h: commodity avg `0.1053` n `12`; crypto_alt avg `-0.0124` n `234`; crypto_major avg `0.0176` n `8`; equity avg `0.1153` n `141`; fx avg `-0.0256` n `6`; index avg `0.0212` n `26`; metal avg `0.038` n `20`; unknown avg `1.6934` n `952`
- 4h: commodity avg `0.0794` n `12`; crypto_alt avg `-2.5023` n `234`; crypto_major avg `-1.7994` n `8`; equity avg `-1.406` n `141`; fx avg `-0.0117` n `6`; index avg `-0.1642` n `26`; metal avg `-0.4437` n `20`; unknown avg `114.2508` n `936`
- 24h: commodity avg `-0.3763` n `12`; crypto_alt avg `-0.87` n `234`; crypto_major avg `-1.2843` n `8`; equity avg `-1.3528` n `141`; fx avg `0.0427` n `6`; index avg `-0.1312` n `26`; metal avg `-0.6817` n `20`; unknown avg `13.6168` n `811`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
