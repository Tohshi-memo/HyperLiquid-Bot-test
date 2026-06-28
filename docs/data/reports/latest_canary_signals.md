# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T05:22:27.968537+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0366` n `12`; crypto_alt avg `-0.0952` n `228`; crypto_major avg `-0.0293` n `8`; equity avg `-0.0187` n `88`; fx avg `-0.0018` n `6`; index avg `-0.0027` n `23`; metal avg `-0.0104` n `20`; unknown avg `-0.2157` n `764`
- 1h: commodity avg `0.0816` n `12`; crypto_alt avg `-0.2661` n `228`; crypto_major avg `-0.326` n `8`; equity avg `-0.0711` n `88`; fx avg `0.0005` n `6`; index avg `-0.0115` n `23`; metal avg `-0.0451` n `20`; unknown avg `0.0825` n `756`
- 4h: commodity avg `-0.2096` n `12`; crypto_alt avg `0.1324` n `228`; crypto_major avg `-0.2662` n `8`; equity avg `-0.0004` n `88`; fx avg `-0.0051` n `6`; index avg `0.0023` n `23`; metal avg `-0.0012` n `20`; unknown avg `15.3333` n `714`
- 24h: commodity avg `0.2607` n `12`; crypto_alt avg `-0.4954` n `228`; crypto_major avg `-1.4258` n `8`; equity avg `0.0063` n `88`; fx avg `-0.0157` n `6`; index avg `-0.116` n `23`; metal avg `-0.0547` n `20`; unknown avg `16.3756` n `666`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2205`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1872`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
