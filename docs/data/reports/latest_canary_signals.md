# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T10:27:00.559132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1543` n `13`; crypto_alt avg `0.1937` n `239`; crypto_major avg `0.0326` n `8`; equity avg `0.2794` n `158`; fx avg `-0.0005` n `6`; index avg `0.0265` n `27`; metal avg `0.0327` n `20`; unknown avg `-0.0258` n `1259`
- 1h: commodity avg `-0.06` n `13`; crypto_alt avg `0.3894` n `239`; crypto_major avg `-0.322` n `8`; equity avg `0.6577` n `158`; fx avg `-0.0022` n `6`; index avg `0.0795` n `27`; metal avg `0.0607` n `20`; unknown avg `-0.1298` n `1255`
- 4h: commodity avg `0.0165` n `13`; crypto_alt avg `0.6684` n `239`; crypto_major avg `-0.4152` n `8`; equity avg `0.4544` n `158`; fx avg `0.0768` n `6`; index avg `0.0535` n `27`; metal avg `-0.097` n `20`; unknown avg `1.0736` n `1129`
- 24h: commodity avg `-0.1371` n `13`; crypto_alt avg `-1.4942` n `239`; crypto_major avg `-3.4638` n `8`; equity avg `-0.0949` n `158`; fx avg `-0.0905` n `6`; index avg `-0.0078` n `27`; metal avg `0.3068` n `20`; unknown avg `0.212` n `1030`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
