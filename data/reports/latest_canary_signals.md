# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T23:07:32.220335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.2672` n `228`; crypto_major avg `-0.3059` n `8`; equity avg `-0.1827` n `78`; fx avg `0.0026` n `6`; index avg `-0.037` n `23`; metal avg `0.0562` n `18`; unknown avg `1.8614` n `702`
- 1h: commodity avg `-0.0759` n `12`; crypto_alt avg `-0.1739` n `228`; crypto_major avg `-0.0585` n `8`; equity avg `-0.217` n `78`; fx avg `-0.002` n `6`; index avg `-0.0413` n `23`; metal avg `0.1307` n `18`; unknown avg `3.4846` n `702`
- 4h: commodity avg `-0.1455` n `12`; crypto_alt avg `-1.5024` n `228`; crypto_major avg `-1.0668` n `8`; equity avg `-0.4253` n `78`; fx avg `-0.0472` n `6`; index avg `-0.1086` n `23`; metal avg `0.0537` n `18`; unknown avg `0.5685` n `694`
- 24h: commodity avg `0.1135` n `12`; crypto_alt avg `-0.5196` n `228`; crypto_major avg `-1.5469` n `8`; equity avg `-0.3112` n `78`; fx avg `-0.1224` n `6`; index avg `-0.1377` n `23`; metal avg `-0.0637` n `18`; unknown avg `0.5724` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
