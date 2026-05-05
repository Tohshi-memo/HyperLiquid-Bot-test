# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T02:00:35.565893+00:00`
- Correlation status: `ready`
- Asset price records: `318`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.062` n `7`; crypto_alt avg `0.1259` n `223`; crypto_major avg `0.02` n `7`; equity avg `-0.0884` n `47`; fx avg `-0.0016` n `4`; index avg `0.0092` n `6`; metal avg `0.1692` n `7`; unknown avg `0.0346` n `312`
- 1h: commodity avg `-0.1158` n `7`; crypto_alt avg `0.4347` n `223`; crypto_major avg `0.1596` n `7`; equity avg `0.0244` n `47`; fx avg `-0.0051` n `4`; index avg `0.0492` n `6`; metal avg `0.2119` n `7`; unknown avg `0.0654` n `312`
- 4h: commodity avg `-0.2219` n `7`; crypto_alt avg `0.0427` n `223`; crypto_major avg `-0.1247` n `7`; equity avg `-0.0157` n `47`; fx avg `-0.0096` n `4`; index avg `-0.0029` n `6`; metal avg `0.3843` n `7`; unknown avg `-0.0853` n `312`
- 24h: commodity avg `1.1929` n `7`; crypto_alt avg `1.3993` n `223`; crypto_major avg `-0.078` n `7`; equity avg `-0.7924` n `47`; fx avg `-0.0497` n `4`; index avg `-0.2082` n `6`; metal avg `-1.9641` n `7`; unknown avg `-1.5305` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2307`, n `314`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2244`, n `314`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1561`, n `310`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.154`, n `310`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1532`, n `314`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1442`, n `314`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1391`, n `314`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1304`, n `314`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1234`, n `310`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1225`, n `314`, weak_sample_signal
