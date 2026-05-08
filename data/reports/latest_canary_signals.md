# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T05:52:12.148551+00:00`
- Correlation status: `ready`
- Asset price records: `619`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `-0.001` n `228`; crypto_major avg `-0.0476` n `8`; equity avg `-0.1814` n `65`; fx avg `0.0191` n `5`; index avg `-0.0056` n `23`; metal avg `-0.0178` n `18`; unknown avg `-0.385` n `365`
- 1h: commodity avg `-0.1103` n `12`; crypto_alt avg `0.0432` n `228`; crypto_major avg `0.0856` n `8`; equity avg `0.057` n `65`; fx avg `0.0078` n `5`; index avg `0.0734` n `23`; metal avg `0.3981` n `18`; unknown avg `-0.7878` n `365`
- 4h: commodity avg `-0.1713` n `12`; crypto_alt avg `0.4257` n `228`; crypto_major avg `-0.0212` n `8`; equity avg `0.1626` n `65`; fx avg `0.0784` n `5`; index avg `0.0751` n `23`; metal avg `0.3314` n `18`; unknown avg `-0.8759` n `365`
- 24h: commodity avg `0.3765` n `12`; crypto_alt avg `1.2434` n `228`; crypto_major avg `-1.5476` n `8`; equity avg `-1.1552` n `65`; fx avg `0.2549` n `5`; index avg `-0.64` n `23`; metal avg `0.6656` n `18`; unknown avg `-0.2079` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1231`, n `615`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1211`, n `611`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1206`, n `611`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1159`, n `615`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `615`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `615`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `611`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `611`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0802`, n `611`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0747`, n `615`, weak_sample_signal
