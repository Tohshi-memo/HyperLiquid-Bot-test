# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T06:37:13.723353+00:00`
- Correlation status: `ready`
- Asset price records: `622`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.03` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1164` n `12`; crypto_alt avg `-0.1556` n `228`; crypto_major avg `-0.0897` n `8`; equity avg `0.0607` n `65`; fx avg `0.0075` n `5`; index avg `0.0081` n `23`; metal avg `0.0719` n `18`; unknown avg `0.0901` n `375`
- 1h: commodity avg `-0.3037` n `12`; crypto_alt avg `-0.3706` n `228`; crypto_major avg `-0.3738` n `8`; equity avg `0.0077` n `65`; fx avg `0.0701` n `5`; index avg `0.0516` n `23`; metal avg `0.2153` n `18`; unknown avg `-0.0789` n `355`
- 4h: commodity avg `-0.6313` n `12`; crypto_alt avg `0.1221` n `228`; crypto_major avg `-0.2494` n `8`; equity avg `0.5479` n `65`; fx avg `0.0998` n `5`; index avg `0.216` n `23`; metal avg `0.8693` n `18`; unknown avg `-0.0667` n `355`
- 24h: commodity avg `0.1473` n `12`; crypto_alt avg `0.7776` n `228`; crypto_major avg `-2.0944` n `8`; equity avg `-0.9477` n `65`; fx avg `0.2855` n `5`; index avg `-0.6034` n `23`; metal avg `0.3388` n `18`; unknown avg `-0.3815` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1322`, n `614`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1314`, n `614`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1208`, n `618`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1128`, n `618`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `618`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0946`, n `618`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0847`, n `614`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `614`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0814`, n `614`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0695`, n `618`, weak_sample_signal
