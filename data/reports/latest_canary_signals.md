# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T11:45:27.925492+00:00`
- Correlation status: `ready`
- Asset price records: `357`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2209` n `7`; crypto_alt avg `0.0993` n `223`; crypto_major avg `0.1107` n `7`; equity avg `0.0424` n `47`; fx avg `-0.0061` n `4`; index avg `0.0223` n `6`; metal avg `0.1423` n `7`; unknown avg `0.029` n `312`
- 1h: commodity avg `-0.1162` n `7`; crypto_alt avg `0.1375` n `223`; crypto_major avg `0.299` n `7`; equity avg `0.1475` n `47`; fx avg `0.0032` n `4`; index avg `-0.0592` n `6`; metal avg `0.3659` n `7`; unknown avg `-0.0735` n `312`
- 4h: commodity avg `0.0415` n `7`; crypto_alt avg `0.1658` n `223`; crypto_major avg `0.2205` n `7`; equity avg `0.1219` n `47`; fx avg `0.0678` n `4`; index avg `0.0334` n `6`; metal avg `0.2123` n `7`; unknown avg `0.1469` n `312`
- 24h: commodity avg `0.1146` n `7`; crypto_alt avg `2.4416` n `223`; crypto_major avg `2.2421` n `7`; equity avg `0.7122` n `47`; fx avg `0.0585` n `4`; index avg `0.3216` n `6`; metal avg `0.9374` n `7`; unknown avg `-0.2143` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2156`, n `353`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2085`, n `353`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1365`, n `353`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1322`, n `353`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1195`, n `353`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1113`, n `353`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `353`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `353`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1049`, n `349`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0919`, n `349`, weak_sample_signal
