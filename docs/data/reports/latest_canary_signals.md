# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T01:22:23.749081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.5` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.135` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0468` n `12`; crypto_alt avg `0.0555` n `228`; crypto_major avg `-0.07` n `8`; equity avg `0.0108` n `69`; fx avg `-0.004` n `6`; index avg `-0.1203` n `23`; metal avg `0.0124` n `18`; unknown avg `0.0467` n `422`
- 1h: commodity avg `0.1827` n `12`; crypto_alt avg `0.1727` n `228`; crypto_major avg `-0.324` n `8`; equity avg `0.0103` n `69`; fx avg `0.022` n `6`; index avg `0.1876` n `23`; metal avg `-0.282` n `18`; unknown avg `-0.2261` n `422`
- 4h: commodity avg `-1.1119` n `12`; crypto_alt avg `-0.9902` n `228`; crypto_major avg `-0.8999` n `8`; equity avg `-0.3227` n `69`; fx avg `0.0169` n `6`; index avg `0.2351` n `23`; metal avg `-0.4518` n `18`; unknown avg `-0.5713` n `422`
- 24h: commodity avg `0.7849` n `12`; crypto_alt avg `-3.8498` n `228`; crypto_major avg `-5.4257` n `8`; equity avg `1.6117` n `69`; fx avg `0.083` n `6`; index avg `1.4082` n `23`; metal avg `-0.4399` n `18`; unknown avg `-0.6763` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
