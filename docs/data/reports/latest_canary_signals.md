# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T22:52:29.123715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0155` n `13`; crypto_alt avg `0.1024` n `236`; crypto_major avg `0.0265` n `8`; equity avg `-0.0183` n `151`; fx avg `0.0015` n `6`; index avg `0.0146` n `26`; metal avg `0.001` n `20`; unknown avg `1.2057` n `1193`
- 1h: commodity avg `-0.0516` n `13`; crypto_alt avg `0.2951` n `236`; crypto_major avg `0.1295` n `8`; equity avg `-0.1801` n `151`; fx avg `-0.0075` n `6`; index avg `-0.0023` n `26`; metal avg `-0.0018` n `20`; unknown avg `2.0811` n `1189`
- 4h: commodity avg `-0.0451` n `13`; crypto_alt avg `1.0804` n `236`; crypto_major avg `0.9975` n `8`; equity avg `-0.3119` n `151`; fx avg `0.003` n `6`; index avg `-0.0221` n `26`; metal avg `0.079` n `20`; unknown avg `0.9363` n `1107`
- 24h: commodity avg `0.4145` n `13`; crypto_alt avg `-1.3844` n `236`; crypto_major avg `-1.2739` n `8`; equity avg `-4.0865` n `151`; fx avg `0.014` n `6`; index avg `-0.6277` n `26`; metal avg `-0.07` n `20`; unknown avg `39.7595` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1653`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1156`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1123`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0882`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0762`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0712`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0707`, n `666`, weak_sample_signal
