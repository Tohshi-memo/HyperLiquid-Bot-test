# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T10:15:49.493946+00:00`
- Correlation status: `ready`
- Asset price records: `445`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.4856` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0665` n `7`; crypto_alt avg `-0.0526` n `223`; crypto_major avg `-0.0146` n `7`; equity avg `0.0589` n `47`; fx avg `0.0097` n `4`; index avg `-0.0179` n `6`; metal avg `0.0173` n `7`; unknown avg `-0.0095` n `313`
- 1h: commodity avg `-0.5469` n `7`; crypto_alt avg `0.3186` n `223`; crypto_major avg `0.5064` n `7`; equity avg `0.1392` n `47`; fx avg `0.0042` n `4`; index avg `0.0852` n `6`; metal avg `0.4328` n `7`; unknown avg `0.2305` n `313`
- 4h: commodity avg `-2.0268` n `7`; crypto_alt avg `2.1031` n `223`; crypto_major avg `1.4588` n `7`; equity avg `0.753` n `47`; fx avg `-0.0603` n `4`; index avg `0.6194` n `6`; metal avg `1.3101` n `7`; unknown avg `1.8798` n `313`
- 24h: commodity avg `-3.3754` n `7`; crypto_alt avg `4.0469` n `223`; crypto_major avg `3.2355` n `7`; equity avg `3.5967` n `47`; fx avg `-0.5562` n `4`; index avg `2.8371` n `6`; metal avg `2.9262` n `7`; unknown avg `3.3252` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1698`, n `441`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1637`, n `441`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1489`, n `441`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1368`, n `441`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1212`, n `441`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1175`, n `441`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.113`, n `437`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1005`, n `437`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0959`, n `437`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `437`, weak_sample_signal
