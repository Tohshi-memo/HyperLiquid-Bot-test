# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T04:07:32.122698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0396` n `12`; crypto_alt avg `0.225` n `234`; crypto_major avg `0.1368` n `8`; equity avg `-0.0063` n `141`; fx avg `-0.006` n `6`; index avg `-0.0058` n `26`; metal avg `-0.0224` n `20`; unknown avg `1.7802` n `938`
- 1h: commodity avg `0.1017` n `12`; crypto_alt avg `0.0507` n `234`; crypto_major avg `-0.0424` n `8`; equity avg `-0.074` n `141`; fx avg `-0.0197` n `6`; index avg `-0.013` n `26`; metal avg `-0.1111` n `20`; unknown avg `1.3654` n `938`
- 4h: commodity avg `-0.091` n `12`; crypto_alt avg `-0.87` n `234`; crypto_major avg `-0.5425` n `8`; equity avg `0.3053` n `141`; fx avg `-0.1475` n `6`; index avg `0.0705` n `26`; metal avg `-0.0715` n `20`; unknown avg `0.6901` n `938`
- 24h: commodity avg `0.5239` n `12`; crypto_alt avg `2.3679` n `234`; crypto_major avg `0.9858` n `8`; equity avg `0.5607` n `141`; fx avg `-0.1511` n `6`; index avg `0.0509` n `26`; metal avg `-0.1497` n `20`; unknown avg `18.9767` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
