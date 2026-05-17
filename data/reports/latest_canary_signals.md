# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T12:52:12.913174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0175` n `12`; crypto_alt avg `-0.144` n `228`; crypto_major avg `-0.0666` n `8`; equity avg `0.0009` n `65`; fx avg `-0.0015` n `5`; index avg `0.0773` n `23`; metal avg `0.0125` n `18`; unknown avg `0.0102` n `383`
- 1h: commodity avg `0.0362` n `12`; crypto_alt avg `-0.0424` n `228`; crypto_major avg `0.1892` n `8`; equity avg `0.0836` n `65`; fx avg `-0.0179` n `5`; index avg `0.0035` n `23`; metal avg `0.0095` n `18`; unknown avg `-0.0362` n `383`
- 4h: commodity avg `0.0121` n `12`; crypto_alt avg `-0.0567` n `228`; crypto_major avg `0.5779` n `8`; equity avg `0.348` n `65`; fx avg `-0.0156` n `5`; index avg `0.1509` n `23`; metal avg `-0.0225` n `18`; unknown avg `-0.003` n `383`
- 24h: commodity avg `1.793` n `12`; crypto_alt avg `-9.0304` n `228`; crypto_major avg `-2.08` n `8`; equity avg `-2.5231` n `65`; fx avg `-0.1853` n `5`; index avg `-1.6458` n `23`; metal avg `-5.8422` n `18`; unknown avg `550.1026` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
