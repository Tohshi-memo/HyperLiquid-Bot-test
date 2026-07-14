# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T11:52:25.995790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.0015` n `230`; crypto_major avg `0.0274` n `8`; equity avg `-0.0204` n `92`; fx avg `0.015` n `6`; index avg `0.0233` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.0073` n `766`
- 1h: commodity avg `-0.2571` n `12`; crypto_alt avg `0.033` n `230`; crypto_major avg `0.0414` n `8`; equity avg `-0.2319` n `92`; fx avg `0.0163` n `6`; index avg `0.0594` n `25`; metal avg `0.0382` n `20`; unknown avg `0.0255` n `766`
- 4h: commodity avg `-0.0648` n `12`; crypto_alt avg `0.05` n `230`; crypto_major avg `0.4346` n `8`; equity avg `-0.0455` n `92`; fx avg `0.0502` n `6`; index avg `0.0793` n `25`; metal avg `-0.0422` n `20`; unknown avg `0.1095` n `766`
- 24h: commodity avg `1.1973` n `12`; crypto_alt avg `-0.8355` n `230`; crypto_major avg `-0.3375` n `8`; equity avg `-0.7946` n `92`; fx avg `-0.0041` n `6`; index avg `-0.0528` n `25`; metal avg `-0.1543` n `20`; unknown avg `-0.2961` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1663`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
