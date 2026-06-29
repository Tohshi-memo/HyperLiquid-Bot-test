# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T01:22:27.851182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0168` n `12`; crypto_alt avg `-0.3837` n `228`; crypto_major avg `-0.4067` n `8`; equity avg `-0.1893` n `88`; fx avg `-0.0026` n `6`; index avg `-0.0421` n `23`; metal avg `-0.138` n `20`; unknown avg `-0.2018` n `764`
- 1h: commodity avg `0.1451` n `12`; crypto_alt avg `0.2333` n `228`; crypto_major avg `0.2402` n `8`; equity avg `-0.0806` n `88`; fx avg `-0.0033` n `6`; index avg `0.0051` n `23`; metal avg `0.0507` n `20`; unknown avg `-0.1076` n `764`
- 4h: commodity avg `-0.0815` n `12`; crypto_alt avg `-0.0082` n `228`; crypto_major avg `-0.1176` n `8`; equity avg `-0.5424` n `88`; fx avg `0.0314` n `6`; index avg `-0.1862` n `23`; metal avg `-0.2629` n `20`; unknown avg `1.2676` n `762`
- 24h: commodity avg `-0.4981` n `12`; crypto_alt avg `-0.5396` n `228`; crypto_major avg `-0.7802` n `8`; equity avg `-0.1754` n `88`; fx avg `-0.0277` n `6`; index avg `-0.0572` n `23`; metal avg `-0.2662` n `20`; unknown avg `15.4049` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.189`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1873`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
