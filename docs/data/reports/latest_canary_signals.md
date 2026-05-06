# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T09:45:24.673489+00:00`
- Correlation status: `ready`
- Asset price records: `443`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.3354` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.242` n `7`; crypto_alt avg `0.1155` n `223`; crypto_major avg `0.0149` n `7`; equity avg `-0.0111` n `47`; fx avg `0.004` n `4`; index avg `-0.0362` n `6`; metal avg `-0.045` n `7`; unknown avg `1.0718` n `313`
- 1h: commodity avg `-1.2564` n `7`; crypto_alt avg `0.3602` n `223`; crypto_major avg `0.3548` n `7`; equity avg `0.4797` n `47`; fx avg `-0.0206` n `4`; index avg `0.7873` n `6`; metal avg `0.7623` n `7`; unknown avg `1.1542` n `313`
- 4h: commodity avg `-1.8507` n `7`; crypto_alt avg `1.9258` n `223`; crypto_major avg `1.4847` n `7`; equity avg `0.8596` n `47`; fx avg `-0.1244` n `4`; index avg `0.6585` n `6`; metal avg `1.0254` n `7`; unknown avg `2.0959` n `311`
- 24h: commodity avg `-3.0051` n `7`; crypto_alt avg `4.0447` n `223`; crypto_major avg `3.2245` n `7`; equity avg `3.382` n `47`; fx avg `-0.5573` n `4`; index avg `2.8296` n `6`; metal avg `2.5975` n `7`; unknown avg `3.2138` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1708`, n `439`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1647`, n `439`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1461`, n `439`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.133`, n `439`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1219`, n `439`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1182`, n `439`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1078`, n `435`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0959`, n `435`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `435`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0932`, n `435`, weak_sample_signal
