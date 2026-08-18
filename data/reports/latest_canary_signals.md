# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T12:37:30.531148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0145` n `12`; crypto_alt avg `0.0039` n `230`; crypto_major avg `-0.1399` n `8`; equity avg `-0.2028` n `114`; fx avg `-0.0012` n `6`; index avg `-0.0357` n `25`; metal avg `-0.0452` n `20`; unknown avg `0.0388` n `795`
- 1h: commodity avg `0.0342` n `12`; crypto_alt avg `-0.018` n `230`; crypto_major avg `-0.237` n `8`; equity avg `-0.1939` n `114`; fx avg `0.0019` n `6`; index avg `-0.0196` n `25`; metal avg `0.0164` n `20`; unknown avg `-0.0192` n `795`
- 4h: commodity avg `0.0952` n `12`; crypto_alt avg `0.1491` n `230`; crypto_major avg `-0.0663` n `8`; equity avg `-0.4317` n `114`; fx avg `-0.0267` n `6`; index avg `-0.045` n `25`; metal avg `0.0091` n `20`; unknown avg `-0.0642` n `795`
- 24h: commodity avg `0.5539` n `12`; crypto_alt avg `-0.6127` n `230`; crypto_major avg `0.2002` n `8`; equity avg `-2.3218` n `114`; fx avg `-0.0492` n `6`; index avg `-0.4888` n `25`; metal avg `-0.1297` n `20`; unknown avg `-0.0475` n `760`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
