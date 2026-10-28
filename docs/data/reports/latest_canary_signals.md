# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T17:07:32.274169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.59` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0609` n `13`; crypto_alt avg `-0.2687` n `238`; crypto_major avg `-0.1935` n `8`; equity avg `-0.1159` n `155`; fx avg `0.0006` n `6`; index avg `-0.02` n `27`; metal avg `-0.0588` n `20`; unknown avg `1.6422` n `1232`
- 1h: commodity avg `-0.12` n `13`; crypto_alt avg `-0.2088` n `238`; crypto_major avg `0.0264` n `8`; equity avg `0.0131` n `155`; fx avg `0.014` n `6`; index avg `0.0238` n `27`; metal avg `0.0043` n `20`; unknown avg `1.1278` n `1232`
- 4h: commodity avg `0.1927` n `13`; crypto_alt avg `-0.3813` n `238`; crypto_major avg `-0.3038` n `8`; equity avg `-0.0898` n `155`; fx avg `0.1151` n `6`; index avg `0.0464` n `27`; metal avg `-0.1668` n `20`; unknown avg `4.3194` n `1150`
- 24h: commodity avg `0.5951` n `13`; crypto_alt avg `-0.2941` n `238`; crypto_major avg `-0.2119` n `8`; equity avg `1.135` n `154`; fx avg `0.2579` n `6`; index avg `0.2897` n `27`; metal avg `-0.181` n `20`; unknown avg `2.9414` n `1098`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1715`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
