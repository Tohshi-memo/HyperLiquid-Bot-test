# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T13:22:31.390241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `13`; crypto_alt avg `-0.2539` n `236`; crypto_major avg `-0.0673` n `8`; equity avg `-0.038` n `151`; fx avg `-0.0001` n `6`; index avg `-0.0085` n `26`; metal avg `0.0011` n `20`; unknown avg `-0.2046` n `1193`
- 1h: commodity avg `-0.0139` n `13`; crypto_alt avg `-0.8126` n `236`; crypto_major avg `-0.2817` n `8`; equity avg `-0.0861` n `151`; fx avg `-0.0143` n `6`; index avg `-0.0132` n `26`; metal avg `-0.0118` n `20`; unknown avg `-0.1011` n `1191`
- 4h: commodity avg `-0.0115` n `13`; crypto_alt avg `-1.3757` n `236`; crypto_major avg `-0.7154` n `8`; equity avg `-0.1752` n `151`; fx avg `0.024` n `6`; index avg `-0.0295` n `26`; metal avg `-0.0166` n `20`; unknown avg `2.9802` n `1183`
- 24h: commodity avg `0.5767` n `13`; crypto_alt avg `-3.3658` n `236`; crypto_major avg `-1.7518` n `8`; equity avg `-3.301` n `151`; fx avg `0.0236` n `6`; index avg `-0.5609` n `26`; metal avg `-0.0966` n `20`; unknown avg `10.3147` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1756`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1478`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.118`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1178`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0673`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0633`, n `666`, weak_sample_signal
