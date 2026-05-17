# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T22:37:18.148236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1028` n `12`; crypto_alt avg `-0.1355` n `228`; crypto_major avg `-0.0569` n `8`; equity avg `0.2927` n `66`; fx avg `-0.0006` n `5`; index avg `-0.0046` n `23`; metal avg `0.265` n `18`; unknown avg `0.179` n `383`
- 1h: commodity avg `0.1476` n `12`; crypto_alt avg `-0.8196` n `228`; crypto_major avg `-0.5384` n `8`; equity avg `0.2807` n `66`; fx avg `0.0062` n `5`; index avg `-0.0092` n `23`; metal avg `0.583` n `18`; unknown avg `0.1849` n `383`
- 4h: commodity avg `-0.0351` n `12`; crypto_alt avg `0.0382` n `228`; crypto_major avg `0.597` n `8`; equity avg `0.6915` n `66`; fx avg `-0.0187` n `5`; index avg `0.1435` n `23`; metal avg `0.5609` n `18`; unknown avg `0.348` n `383`
- 24h: commodity avg `1.8183` n `12`; crypto_alt avg `-9.5823` n `228`; crypto_major avg `-1.6392` n `8`; equity avg `-2.2314` n `65`; fx avg `-0.1739` n `5`; index avg `-1.4614` n `23`; metal avg `-5.377` n `18`; unknown avg `550.7411` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
