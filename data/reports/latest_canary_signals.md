# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T09:45:28.614467+00:00`
- Correlation status: `ready`
- Asset price records: `349`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0214` n `7`; crypto_alt avg `-0.1884` n `223`; crypto_major avg `-0.1622` n `7`; equity avg `-0.0666` n `47`; fx avg `0.0104` n `4`; index avg `0.0393` n `6`; metal avg `0.1123` n `7`; unknown avg `-0.1289` n `312`
- 1h: commodity avg `0.0976` n `7`; crypto_alt avg `-0.0759` n `223`; crypto_major avg `-0.2364` n `7`; equity avg `-0.0044` n `47`; fx avg `0.0517` n `4`; index avg `-0.1262` n `6`; metal avg `0.1565` n `7`; unknown avg `0.0127` n `312`
- 4h: commodity avg `-0.135` n `7`; crypto_alt avg `0.2682` n `223`; crypto_major avg `-0.2422` n `7`; equity avg `0.1946` n `47`; fx avg `0.0682` n `4`; index avg `0.1533` n `6`; metal avg `0.4429` n `7`; unknown avg `0.1127` n `310`
- 24h: commodity avg `0.542` n `7`; crypto_alt avg `0.5437` n `223`; crypto_major avg `0.0578` n `7`; equity avg `0.0521` n `47`; fx avg `0.0273` n `4`; index avg `0.1443` n `6`; metal avg `0.1171` n `7`; unknown avg `-1.0319` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2173`, n `345`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2101`, n `345`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1393`, n `345`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1347`, n `345`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1174`, n `345`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1113`, n `345`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1063`, n `345`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1056`, n `345`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1034`, n `341`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0927`, n `341`, weak_sample_signal
