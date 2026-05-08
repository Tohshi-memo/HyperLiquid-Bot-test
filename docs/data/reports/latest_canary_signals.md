# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T10:22:14.916788+00:00`
- Correlation status: `ready`
- Asset price records: `637`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.009` n `12`; crypto_alt avg `-0.1768` n `228`; crypto_major avg `-0.1581` n `8`; equity avg `-0.0012` n `65`; fx avg `0.0059` n `5`; index avg `-0.0229` n `23`; metal avg `0.0787` n `18`; unknown avg `-0.04` n `375`
- 1h: commodity avg `0.3679` n `12`; crypto_alt avg `-0.3967` n `228`; crypto_major avg `-0.3361` n `8`; equity avg `-0.1806` n `65`; fx avg `0.0353` n `5`; index avg `-0.0547` n `23`; metal avg `-0.0954` n `18`; unknown avg `-0.2095` n `375`
- 4h: commodity avg `0.3136` n `12`; crypto_alt avg `0.4116` n `228`; crypto_major avg `0.3618` n `8`; equity avg `0.6554` n `65`; fx avg `0.0455` n `5`; index avg `0.1505` n `23`; metal avg `-0.1705` n `18`; unknown avg `0.6142` n `375`
- 24h: commodity avg `1.3245` n `12`; crypto_alt avg `0.9978` n `228`; crypto_major avg `-1.5351` n `8`; equity avg `-0.6165` n `65`; fx avg `0.2502` n `5`; index avg `-0.3915` n `23`; metal avg `-0.434` n `18`; unknown avg `-0.0808` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.141`, n `629`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1395`, n `629`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1153`, n `633`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1002`, n `633`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0979`, n `633`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0967`, n `633`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0948`, n `629`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0847`, n `629`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `629`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `633`, weak_sample_signal
