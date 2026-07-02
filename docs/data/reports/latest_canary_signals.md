# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T01:07:28.216939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `12`; crypto_alt avg `0.243` n `228`; crypto_major avg `0.0344` n `8`; equity avg `0.3325` n `88`; fx avg `0.0012` n `6`; index avg `0.0869` n `25`; metal avg `0.115` n `20`; unknown avg `-0.1273` n `763`
- 1h: commodity avg `-0.016` n `12`; crypto_alt avg `0.1498` n `228`; crypto_major avg `-0.1928` n `8`; equity avg `0.292` n `88`; fx avg `0.0102` n `6`; index avg `0.0811` n `25`; metal avg `0.2493` n `20`; unknown avg `0.9` n `763`
- 4h: commodity avg `-0.1159` n `12`; crypto_alt avg `-0.2268` n `228`; crypto_major avg `-0.7314` n `8`; equity avg `-0.1171` n `88`; fx avg `0.0472` n `6`; index avg `-0.0556` n `25`; metal avg `0.3043` n `20`; unknown avg `23.9102` n `763`
- 24h: commodity avg `-0.6538` n `12`; crypto_alt avg `1.9876` n `228`; crypto_major avg `1.3338` n `8`; equity avg `-1.4291` n `88`; fx avg `-0.0301` n `6`; index avg `-0.4658` n `25`; metal avg `0.6572` n `20`; unknown avg `25.2597` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
