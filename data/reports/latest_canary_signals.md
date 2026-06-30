# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T18:22:27.565238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.76` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1539` n `12`; crypto_alt avg `0.2827` n `228`; crypto_major avg `0.4085` n `8`; equity avg `0.0851` n `88`; fx avg `-0.0102` n `6`; index avg `0.0053` n `23`; metal avg `-0.0045` n `20`; unknown avg `-0.0601` n `765`
- 1h: commodity avg `-0.182` n `12`; crypto_alt avg `0.2006` n `228`; crypto_major avg `0.3457` n `8`; equity avg `0.0842` n `88`; fx avg `-0.0024` n `6`; index avg `-0.0028` n `23`; metal avg `0.0971` n `20`; unknown avg `0.0598` n `765`
- 4h: commodity avg `-0.3252` n `12`; crypto_alt avg `-0.2161` n `228`; crypto_major avg `-0.091` n `8`; equity avg `0.2369` n `88`; fx avg `0.024` n `6`; index avg `0.0789` n `23`; metal avg `-0.3261` n `20`; unknown avg `-0.1164` n `765`
- 24h: commodity avg `0.0062` n `12`; crypto_alt avg `-2.4448` n `228`; crypto_major avg `-2.3395` n `8`; equity avg `1.2154` n `88`; fx avg `0.1418` n `6`; index avg `0.3201` n `23`; metal avg `0.1686` n `20`; unknown avg `8.392` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
