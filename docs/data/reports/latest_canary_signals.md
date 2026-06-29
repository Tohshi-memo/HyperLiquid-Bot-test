# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T10:07:31.335888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.052` n `12`; crypto_alt avg `0.1744` n `228`; crypto_major avg `0.2754` n `8`; equity avg `0.0923` n `88`; fx avg `0.0002` n `6`; index avg `0.0163` n `23`; metal avg `0.0388` n `20`; unknown avg `0.4567` n `764`
- 1h: commodity avg `0.0706` n `12`; crypto_alt avg `0.4089` n `228`; crypto_major avg `0.4484` n `8`; equity avg `0.1463` n `88`; fx avg `0.0316` n `6`; index avg `0.0093` n `23`; metal avg `-0.2337` n `20`; unknown avg `0.2283` n `764`
- 4h: commodity avg `0.033` n `12`; crypto_alt avg `0.216` n `228`; crypto_major avg `0.0679` n `8`; equity avg `0.3523` n `88`; fx avg `0.088` n `6`; index avg `0.06` n `23`; metal avg `-0.3905` n `20`; unknown avg `0.1595` n `764`
- 24h: commodity avg `-0.3286` n `12`; crypto_alt avg `0.5025` n `228`; crypto_major avg `0.2286` n `8`; equity avg `0.5163` n `88`; fx avg `0.0628` n `6`; index avg `0.0858` n `23`; metal avg `-0.5246` n `20`; unknown avg `0.2132` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
