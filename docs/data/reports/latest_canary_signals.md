# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T18:07:28.250142+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0275` n `12`; crypto_alt avg `0.0562` n `228`; crypto_major avg `0.065` n `8`; equity avg `0.0314` n `88`; fx avg `0.0` n `6`; index avg `0.0003` n `23`; metal avg `0.008` n `20`; unknown avg `-0.0345` n `764`
- 1h: commodity avg `-0.0971` n `12`; crypto_alt avg `-0.2536` n `228`; crypto_major avg `-0.2179` n `8`; equity avg `-0.0491` n `88`; fx avg `0.0094` n `6`; index avg `-0.0002` n `23`; metal avg `0.0036` n `20`; unknown avg `0.1155` n `764`
- 4h: commodity avg `0.0031` n `12`; crypto_alt avg `-0.2654` n `228`; crypto_major avg `-0.4269` n `8`; equity avg `-0.0267` n `88`; fx avg `-0.0114` n `6`; index avg `-0.0063` n `23`; metal avg `-0.0363` n `20`; unknown avg `0.331` n `764`
- 24h: commodity avg `0.313` n `12`; crypto_alt avg `-0.5874` n `228`; crypto_major avg `-1.2163` n `8`; equity avg `0.1128` n `88`; fx avg `-0.0249` n `6`; index avg `-0.0459` n `23`; metal avg `-0.0387` n `20`; unknown avg `14.7246` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
