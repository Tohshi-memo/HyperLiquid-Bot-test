# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T09:37:31.589337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2165` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5504` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0541` n `12`; crypto_alt avg `0.2903` n `234`; crypto_major avg `0.1907` n `8`; equity avg `-0.0377` n `141`; fx avg `0.0065` n `6`; index avg `-0.0224` n `26`; metal avg `-0.0083` n `20`; unknown avg `0.4946` n `963`
- 1h: commodity avg `-0.1261` n `12`; crypto_alt avg `0.31` n `234`; crypto_major avg `0.1798` n `8`; equity avg `-0.2085` n `141`; fx avg `-0.0104` n `6`; index avg `-0.0468` n `26`; metal avg `0.0372` n `20`; unknown avg `0.1008` n `961`
- 4h: commodity avg `-0.5063` n `12`; crypto_alt avg `2.7705` n `234`; crypto_major avg `1.7102` n `8`; equity avg `1.0731` n `141`; fx avg `-0.0428` n `6`; index avg `0.164` n `26`; metal avg `0.1598` n `20`; unknown avg `1.9766` n `927`
- 24h: commodity avg `-0.6097` n `12`; crypto_alt avg `1.869` n `234`; crypto_major avg `1.3102` n `8`; equity avg `-0.0945` n `141`; fx avg `-0.0859` n `6`; index avg `-0.044` n `26`; metal avg `-0.1542` n `20`; unknown avg `51.6509` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
