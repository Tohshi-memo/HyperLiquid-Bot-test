# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T20:52:32.040130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `13`; crypto_alt avg `-0.0988` n `236`; crypto_major avg `-0.2273` n `8`; equity avg `0.0086` n `151`; fx avg `-0.0003` n `6`; index avg `-0.0058` n `26`; metal avg `-0.0018` n `20`; unknown avg `2.9433` n `1136`
- 1h: commodity avg `-0.0209` n `13`; crypto_alt avg `-0.1179` n `236`; crypto_major avg `-0.148` n `8`; equity avg `0.1648` n `151`; fx avg `-0.0016` n `6`; index avg `0.0061` n `26`; metal avg `-0.0253` n `20`; unknown avg `4.3436` n `1066`
- 4h: commodity avg `-0.0695` n `13`; crypto_alt avg `0.4006` n `236`; crypto_major avg `0.4287` n `8`; equity avg `1.8391` n `151`; fx avg `-0.0079` n `6`; index avg `0.1867` n `26`; metal avg `0.1452` n `20`; unknown avg `1.7295` n `1058`
- 24h: commodity avg `-0.2126` n `13`; crypto_alt avg `0.9461` n `236`; crypto_major avg `0.7498` n `8`; equity avg `0.4576` n `151`; fx avg `0.1732` n `6`; index avg `-0.0155` n `26`; metal avg `0.5397` n `20`; unknown avg `26.2823` n `926`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.1022`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0952`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0848`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0776`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0737`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0702`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0518`, n `666`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0483`, n `666`, weak_sample_signal
