# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T05:22:28.032045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.4071` n `13`; crypto_alt avg `0.0845` n `234`; crypto_major avg `0.0874` n `8`; equity avg `0.0481` n `142`; fx avg `0.0092` n `6`; index avg `0.0128` n `26`; metal avg `0.0083` n `20`; unknown avg `0.4369` n `974`
- 1h: commodity avg `0.3556` n `13`; crypto_alt avg `0.1412` n `234`; crypto_major avg `0.385` n `8`; equity avg `0.3737` n `142`; fx avg `-0.0083` n `6`; index avg `0.0935` n `26`; metal avg `0.1149` n `20`; unknown avg `0.325` n `972`
- 4h: commodity avg `-0.0054` n `13`; crypto_alt avg `0.5065` n `234`; crypto_major avg `0.3741` n `8`; equity avg `0.9045` n `142`; fx avg `-0.0353` n `6`; index avg `0.2184` n `26`; metal avg `0.1698` n `20`; unknown avg `0.4776` n `966`
- 24h: commodity avg `-0.2919` n `13`; crypto_alt avg `1.4113` n `234`; crypto_major avg `1.4145` n `8`; equity avg `1.0537` n `142`; fx avg `0.1735` n `6`; index avg `0.303` n `26`; metal avg `0.1111` n `20`; unknown avg `774.5437` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
