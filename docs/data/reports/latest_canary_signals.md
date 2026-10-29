# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T17:22:30.816147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1477` n `13`; crypto_alt avg `-0.0525` n `238`; crypto_major avg `-0.0704` n `8`; equity avg `-0.099` n `156`; fx avg `0.0052` n `6`; index avg `-0.021` n `27`; metal avg `-0.0258` n `20`; unknown avg `-0.0247` n `1238`
- 1h: commodity avg `0.0475` n `13`; crypto_alt avg `-0.4122` n `238`; crypto_major avg `-0.4256` n `8`; equity avg `-0.4262` n `156`; fx avg `0.0015` n `6`; index avg `-0.0343` n `27`; metal avg `0.0071` n `20`; unknown avg `7.3336` n `1232`
- 4h: commodity avg `0.1847` n `13`; crypto_alt avg `1.2924` n `238`; crypto_major avg `1.1738` n `8`; equity avg `0.2706` n `156`; fx avg `0.153` n `6`; index avg `-0.043` n `27`; metal avg `-0.0022` n `20`; unknown avg `0.474` n `1132`
- 24h: commodity avg `-0.7258` n `13`; crypto_alt avg `1.4133` n `238`; crypto_major avg `2.6906` n `8`; equity avg `-0.7105` n `155`; fx avg `0.0249` n `6`; index avg `-0.1388` n `27`; metal avg `-0.4285` n `20`; unknown avg `9.5738` n `946`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
