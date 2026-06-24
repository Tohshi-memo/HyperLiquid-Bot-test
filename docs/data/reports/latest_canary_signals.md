# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T20:37:30.388436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `0.0719` n `228`; crypto_major avg `0.1597` n `8`; equity avg `0.2346` n `86`; fx avg `0.0003` n `6`; index avg `0.0413` n `23`; metal avg `0.031` n `20`; unknown avg `1.0309` n `764`
- 1h: commodity avg `-0.0435` n `12`; crypto_alt avg `1.5846` n `228`; crypto_major avg `1.7422` n `8`; equity avg `2.1195` n `86`; fx avg `-0.011` n `6`; index avg `0.4997` n `23`; metal avg `0.351` n `20`; unknown avg `4.9288` n `764`
- 4h: commodity avg `-0.1717` n `12`; crypto_alt avg `0.087` n `228`; crypto_major avg `0.7046` n `8`; equity avg `1.2717` n `86`; fx avg `-0.0011` n `6`; index avg `0.366` n `23`; metal avg `-0.3297` n `20`; unknown avg `1.228` n `764`
- 24h: commodity avg `-0.5971` n `12`; crypto_alt avg `-2.7745` n `228`; crypto_major avg `-2.1942` n `8`; equity avg `3.8605` n `86`; fx avg `0.0525` n `6`; index avg `0.5148` n `23`; metal avg `-1.6276` n `20`; unknown avg `-0.5511` n `724`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
