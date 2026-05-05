# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T01:45:23.690570+00:00`
- Correlation status: `ready`
- Asset price records: `317`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.047` n `7`; crypto_alt avg `-0.0033` n `223`; crypto_major avg `-0.0287` n `7`; equity avg `0.105` n `47`; fx avg `0.0051` n `4`; index avg `0.0196` n `6`; metal avg `-0.0304` n `7`; unknown avg `0.1481` n `312`
- 1h: commodity avg `-0.0509` n `7`; crypto_alt avg `0.4111` n `223`; crypto_major avg `0.2211` n `7`; equity avg `0.1367` n `47`; fx avg `-0.0035` n `4`; index avg `0.0724` n `6`; metal avg `0.1174` n `7`; unknown avg `0.0423` n `312`
- 4h: commodity avg `-0.1082` n `7`; crypto_alt avg `0.1303` n `223`; crypto_major avg `0.0348` n `7`; equity avg `0.1812` n `47`; fx avg `-0.0035` n `4`; index avg `0.0202` n `6`; metal avg `0.1595` n `7`; unknown avg `0.103` n `312`
- 24h: commodity avg `1.2172` n `7`; crypto_alt avg `2.0208` n `223`; crypto_major avg `0.9167` n `7`; equity avg `-0.4952` n `47`; fx avg `-0.047` n `4`; index avg `-0.1029` n `6`; metal avg `-1.7081` n `7`; unknown avg `-1.401` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2314`, n `313`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2251`, n `313`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1565`, n `309`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1545`, n `309`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1526`, n `313`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1444`, n `313`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1393`, n `313`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1305`, n `313`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1233`, n `309`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1206`, n `313`, weak_sample_signal
