# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T02:37:18.548718+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1615` n `12`; crypto_alt avg `-0.3203` n `228`; crypto_major avg `-0.032` n `8`; equity avg `0.0701` n `66`; fx avg `-0.0038` n `6`; index avg `-0.0204` n `23`; metal avg `-0.1421` n `18`; unknown avg `0.0315` n `383`
- 1h: commodity avg `0.0924` n `12`; crypto_alt avg `-0.3142` n `228`; crypto_major avg `-0.3101` n `8`; equity avg `-0.3211` n `66`; fx avg `0.0051` n `6`; index avg `-0.2034` n `23`; metal avg `-0.5202` n `18`; unknown avg `-0.3999` n `383`
- 4h: commodity avg `0.2611` n `12`; crypto_alt avg `-0.1828` n `228`; crypto_major avg `-0.3333` n `8`; equity avg `-0.6965` n `66`; fx avg `0.1392` n `6`; index avg `-0.533` n `23`; metal avg `-1.0739` n `18`; unknown avg `-0.4455` n `383`
- 24h: commodity avg `0.2076` n `12`; crypto_alt avg `0.4897` n `228`; crypto_major avg `0.0387` n `8`; equity avg `-1.307` n `66`; fx avg `0.231` n `6`; index avg `-0.4419` n `23`; metal avg `0.6087` n `18`; unknown avg `0.214` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
