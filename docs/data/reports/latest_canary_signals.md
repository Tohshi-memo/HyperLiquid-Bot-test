# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T15:52:27.006262+00:00`
- Correlation status: `ready`
- Asset price records: `467`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `8.18` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.5851` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.8395` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.0387` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2025` n `12`; crypto_alt avg `0.4088` n `228`; crypto_major avg `0.2198` n `8`; equity avg `0.1036` n `65`; fx avg `0.0063` n `4`; index avg `-0.0023` n `23`; metal avg `-0.0248` n `18`; unknown avg `0.0689` n `356`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `0.3909` n `228`; crypto_major avg `0.1206` n `8`; equity avg `0.0835` n `65`; fx avg `0.0099` n `4`; index avg `0.0294` n `23`; metal avg `-0.0438` n `18`; unknown avg `0.1978` n `356`
- 4h: commodity avg `0.9673` n `7`; crypto_alt avg `-0.7576` n `223`; crypto_major avg `-1.6178` n `7`; equity avg `-0.6886` n `47`; fx avg `0.0395` n `4`; index avg `-0.5791` n `6`; metal avg `0.2217` n `7`; unknown avg `8.0906` n `313`
- 24h: commodity avg `-2.2126` n `7`; crypto_alt avg `2.975` n `223`; crypto_major avg `0.8694` n `7`; equity avg `1.9945` n `47`; fx avg `-0.4676` n `4`; index avg `1.8771` n `6`; metal avg `2.8449` n `7`; unknown avg `18.2208` n `311`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2546`, n `463`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1768`, n `459`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1633`, n `459`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1617`, n `459`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1608`, n `463`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1526`, n `459`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.136`, n `463`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1226`, n `463`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `463`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1085`, n `463`, weak_sample_signal
