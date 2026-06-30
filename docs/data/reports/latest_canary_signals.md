# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T17:37:27.156244+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.29` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.049` n `12`; crypto_alt avg `0.0251` n `228`; crypto_major avg `-0.0134` n `8`; equity avg `-0.0004` n `88`; fx avg `0.004` n `6`; index avg `-0.0091` n `23`; metal avg `0.0114` n `20`; unknown avg `-0.074` n `765`
- 1h: commodity avg `-0.1464` n `12`; crypto_alt avg `0.2669` n `228`; crypto_major avg `0.4265` n `8`; equity avg `0.1509` n `88`; fx avg `-0.0007` n `6`; index avg `0.0139` n `23`; metal avg `-0.0805` n `20`; unknown avg `0.1678` n `765`
- 4h: commodity avg `-0.1957` n `12`; crypto_alt avg `0.9456` n `228`; crypto_major avg `0.8116` n `8`; equity avg `0.8712` n `88`; fx avg `0.0578` n `6`; index avg `0.1862` n `23`; metal avg `0.0661` n `20`; unknown avg `0.0421` n `765`
- 24h: commodity avg `0.0357` n `12`; crypto_alt avg `-2.6982` n `228`; crypto_major avg `-2.5331` n `8`; equity avg `1.294` n `88`; fx avg `0.136` n `6`; index avg `0.3527` n `23`; metal avg `0.4005` n `20`; unknown avg `8.6681` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
