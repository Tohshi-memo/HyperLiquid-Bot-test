# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T05:22:25.576886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0216` n `12`; crypto_alt avg `-0.0486` n `228`; crypto_major avg `-0.1128` n `8`; equity avg `0.1361` n `86`; fx avg `-0.0043` n `6`; index avg `0.0514` n `23`; metal avg `0.0351` n `20`; unknown avg `261.3356` n `765`
- 1h: commodity avg `0.0138` n `12`; crypto_alt avg `-0.4502` n `228`; crypto_major avg `-0.4199` n `8`; equity avg `-0.0666` n `86`; fx avg `0.0043` n `6`; index avg `0.0119` n `23`; metal avg `-0.0284` n `20`; unknown avg `260.762` n `765`
- 4h: commodity avg `-0.1829` n `12`; crypto_alt avg `-0.6135` n `228`; crypto_major avg `-0.3023` n `8`; equity avg `-1.4678` n `86`; fx avg `-0.03` n `6`; index avg `-0.3587` n `23`; metal avg `-0.3901` n `20`; unknown avg `-0.047` n `749`
- 24h: commodity avg `0.3002` n `12`; crypto_alt avg `-2.9428` n `228`; crypto_major avg `-2.783` n `8`; equity avg `-4.2382` n `86`; fx avg `0.0468` n `6`; index avg `-0.6595` n `23`; metal avg `-0.0652` n `20`; unknown avg `0.5756` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
