# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T00:22:24.563560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0282` n `12`; crypto_alt avg `-0.1482` n `229`; crypto_major avg `-0.1404` n `8`; equity avg `-0.0312` n `92`; fx avg `-0.0031` n `6`; index avg `-0.0045` n `25`; metal avg `-0.002` n `20`; unknown avg `0.3508` n `765`
- 1h: commodity avg `0.0362` n `12`; crypto_alt avg `-0.2371` n `229`; crypto_major avg `-0.2012` n `8`; equity avg `0.0211` n `92`; fx avg `0.0014` n `6`; index avg `-0.0047` n `25`; metal avg `0.0059` n `20`; unknown avg `0.2732` n `765`
- 4h: commodity avg `0.0312` n `12`; crypto_alt avg `0.2115` n `229`; crypto_major avg `0.0406` n `8`; equity avg `0.0972` n `92`; fx avg `0.0005` n `6`; index avg `-0.0237` n `25`; metal avg `0.0258` n `20`; unknown avg `-0.0976` n `765`
- 24h: commodity avg `-0.2256` n `12`; crypto_alt avg `1.0879` n `229`; crypto_major avg `1.0191` n `8`; equity avg `-0.2481` n `92`; fx avg `-0.2179` n `6`; index avg `0.152` n `25`; metal avg `0.1752` n `20`; unknown avg `-0.1737` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
