# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T01:14:52.280548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1003` n `12`; crypto_alt avg `0.185` n `230`; crypto_major avg `0.1465` n `8`; equity avg `0.0444` n `100`; fx avg `-0.0248` n `6`; index avg `-0.0065` n `25`; metal avg `-0.0678` n `20`; unknown avg `-0.1386` n `772`
- 1h: commodity avg `-0.1407` n `12`; crypto_alt avg `0.1552` n `230`; crypto_major avg `0.1246` n `8`; equity avg `-0.0234` n `100`; fx avg `-0.0522` n `6`; index avg `-0.055` n `25`; metal avg `-0.0256` n `20`; unknown avg `-0.1548` n `772`
- 4h: commodity avg `-0.1517` n `12`; crypto_alt avg `-0.4974` n `230`; crypto_major avg `-0.3539` n `8`; equity avg `-0.6857` n `100`; fx avg `-0.0751` n `6`; index avg `-0.1581` n `25`; metal avg `-0.1061` n `20`; unknown avg `-0.7736` n `772`
- 24h: commodity avg `0.5313` n `12`; crypto_alt avg `-1.8871` n `230`; crypto_major avg `-2.4622` n `8`; equity avg `-2.0317` n `99`; fx avg `-0.0996` n `6`; index avg `-0.5087` n `25`; metal avg `-0.8488` n `20`; unknown avg `-0.3868` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0882`, n `666`, weak_sample_signal
