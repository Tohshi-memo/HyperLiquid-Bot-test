# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T23:52:23.373213+00:00`
- Correlation status: `ready`
- Asset price records: `499`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.09` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0213` n `12`; crypto_alt avg `0.1259` n `228`; crypto_major avg `0.0444` n `8`; equity avg `-0.0322` n `65`; fx avg `-0.0005` n `4`; index avg `0.04` n `23`; metal avg `0.102` n `18`; unknown avg `0.0648` n `356`
- 1h: commodity avg `0.0081` n `12`; crypto_alt avg `0.1498` n `228`; crypto_major avg `0.0579` n `8`; equity avg `0.191` n `65`; fx avg `0.0157` n `4`; index avg `0.1079` n `23`; metal avg `0.0623` n `18`; unknown avg `0.1263` n `356`
- 4h: commodity avg `0.3049` n `12`; crypto_alt avg `0.3362` n `228`; crypto_major avg `-0.2262` n `8`; equity avg `-0.0776` n `65`; fx avg `0.0073` n `4`; index avg `-0.0175` n `23`; metal avg `0.0538` n `18`; unknown avg `0.1718` n `356`
- 24h: commodity avg `-1.5839` n `7`; crypto_alt avg `2.4577` n `223`; crypto_major avg `0.4664` n `7`; equity avg `2.0727` n `47`; fx avg `-0.6186` n `4`; index avg `1.6182` n `6`; metal avg `2.7874` n `7`; unknown avg `4.1029` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1304`, n `495`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.117`, n `495`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1045`, n `491`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0935`, n `491`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0864`, n `491`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `491`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0773`, n `491`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0654`, n `495`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0639`, n `491`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0598`, n `491`, weak_sample_signal
