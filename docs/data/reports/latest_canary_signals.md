# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T07:56:06.245771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0225` n `13`; crypto_alt avg `0.0647` n `239`; crypto_major avg `0.1554` n `8`; equity avg `0.0836` n `158`; fx avg `-0.0093` n `6`; index avg `0.0334` n `27`; metal avg `0.0015` n `20`; unknown avg `0.074` n `1258`
- 1h: commodity avg `0.0121` n `13`; crypto_alt avg `0.2693` n `239`; crypto_major avg `0.2087` n `8`; equity avg `0.0898` n `158`; fx avg `0.001` n `6`; index avg `0.0379` n `27`; metal avg `0.0106` n `20`; unknown avg `0.144` n `1252`
- 4h: commodity avg `0.028` n `13`; crypto_alt avg `-0.0081` n `239`; crypto_major avg `0.1494` n `8`; equity avg `0.1419` n `158`; fx avg `0.0148` n `6`; index avg `0.0335` n `27`; metal avg `0.0033` n `20`; unknown avg `-0.2253` n `1208`
- 24h: commodity avg `0.1199` n `13`; crypto_alt avg `-1.7219` n `239`; crypto_major avg `-0.5967` n `8`; equity avg `0.1269` n `158`; fx avg `0.0449` n `6`; index avg `0.0656` n `27`; metal avg `-0.037` n `20`; unknown avg `158.608` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
