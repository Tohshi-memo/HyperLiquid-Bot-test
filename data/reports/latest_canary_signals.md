# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T22:41:28.492946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0428` n `12`; crypto_alt avg `0.0622` n `228`; crypto_major avg `-0.0067` n `8`; equity avg `-0.0719` n `65`; fx avg `-0.0064` n `5`; index avg `-0.0301` n `23`; metal avg `-0.0575` n `18`; unknown avg `0.0527` n `375`
- 1h: commodity avg `-0.2092` n `12`; crypto_alt avg `0.2741` n `228`; crypto_major avg `0.1187` n `8`; equity avg `0.0292` n `65`; fx avg `-0.004` n `5`; index avg `0.083` n `23`; metal avg `-0.062` n `18`; unknown avg `-0.016` n `375`
- 4h: commodity avg `-0.2713` n `12`; crypto_alt avg `0.4402` n `228`; crypto_major avg `0.0919` n `8`; equity avg `0.7177` n `65`; fx avg `0.0015` n `5`; index avg `0.1109` n `23`; metal avg `-0.2389` n `18`; unknown avg `-0.3897` n `375`
- 24h: commodity avg `-0.8545` n `12`; crypto_alt avg `4.1515` n `228`; crypto_major avg `2.0002` n `8`; equity avg `4.5808` n `65`; fx avg `0.2031` n `5`; index avg `1.7137` n `23`; metal avg `1.1225` n `18`; unknown avg `1.0701` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
