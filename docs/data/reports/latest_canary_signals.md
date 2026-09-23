# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T07:22:30.115402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1102` n `12`; crypto_alt avg `0.1097` n `234`; crypto_major avg `0.0877` n `8`; equity avg `0.0185` n `140`; fx avg `-0.0098` n `6`; index avg `-0.0075` n `26`; metal avg `-0.0139` n `20`; unknown avg `0.0182` n `945`
- 1h: commodity avg `0.0954` n `12`; crypto_alt avg `-0.1006` n `234`; crypto_major avg `-0.1152` n `8`; equity avg `-0.0315` n `140`; fx avg `0.0686` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0777` n `20`; unknown avg `-0.0468` n `943`
- 4h: commodity avg `0.0719` n `12`; crypto_alt avg `0.1885` n `234`; crypto_major avg `-0.2085` n `8`; equity avg `0.1161` n `140`; fx avg `0.1217` n `6`; index avg `0.0353` n `26`; metal avg `-0.1477` n `20`; unknown avg `0.2762` n `921`
- 24h: commodity avg `-0.023` n `12`; crypto_alt avg `4.1778` n `234`; crypto_major avg `2.2727` n `8`; equity avg `1.2949` n `140`; fx avg `-0.0952` n `6`; index avg `0.1536` n `26`; metal avg `0.075` n `20`; unknown avg `1.9443` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
