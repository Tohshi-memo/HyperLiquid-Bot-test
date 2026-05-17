# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T18:07:17.139637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `12`; crypto_alt avg `0.1859` n `228`; crypto_major avg `0.1666` n `8`; equity avg `0.0086` n `65`; fx avg `0.0` n `5`; index avg `0.0056` n `23`; metal avg `-0.0462` n `18`; unknown avg `0.0891` n `384`
- 1h: commodity avg `-0.0058` n `12`; crypto_alt avg `0.0514` n `228`; crypto_major avg `0.2081` n `8`; equity avg `0.0938` n `65`; fx avg `0.0` n `5`; index avg `0.0468` n `23`; metal avg `-0.0358` n `18`; unknown avg `0.3752` n `384`
- 4h: commodity avg `0.2476` n `12`; crypto_alt avg `-0.1422` n `228`; crypto_major avg `0.2027` n `8`; equity avg `-0.0663` n `65`; fx avg `0.0322` n `5`; index avg `-0.0391` n `23`; metal avg `-0.0644` n `18`; unknown avg `0.1197` n `383`
- 24h: commodity avg `1.7712` n `12`; crypto_alt avg `-9.5075` n `228`; crypto_major avg `-2.36` n `8`; equity avg `-2.6101` n `65`; fx avg `-0.1543` n `5`; index avg `-1.5966` n `23`; metal avg `-5.885` n `18`; unknown avg `550.082` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
