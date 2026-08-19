# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T14:07:44.423730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `2.2769` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `1.8338` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0645` n `12`; crypto_alt avg `0.2059` n `230`; crypto_major avg `0.2385` n `8`; equity avg `0.0653` n `121`; fx avg `-0.0045` n `6`; index avg `0.0104` n `25`; metal avg `0.0685` n `20`; unknown avg `0.0689` n `792`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `0.1046` n `230`; crypto_major avg `0.225` n `8`; equity avg `-2.0519` n `120`; fx avg `0.0425` n `6`; index avg `-0.1924` n `25`; metal avg `0.2368` n `20`; unknown avg `0.3539` n `792`
- 4h: commodity avg `0.0182` n `12`; crypto_alt avg `0.6701` n `230`; crypto_major avg `0.9982` n `8`; equity avg `-0.8356` n `120`; fx avg `0.0306` n `6`; index avg `0.0199` n `25`; metal avg `0.6729` n `20`; unknown avg `0.5518` n `791`
- 24h: commodity avg `0.3684` n `12`; crypto_alt avg `0.6706` n `230`; crypto_major avg `1.1556` n `8`; equity avg `-2.2158` n `120`; fx avg `-0.1964` n `6`; index avg `-0.1826` n `25`; metal avg `0.2961` n `20`; unknown avg `0.0142` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1634`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
