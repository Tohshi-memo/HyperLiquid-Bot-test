# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T19:52:24.352461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0416` n `12`; crypto_alt avg `0.0473` n `230`; crypto_major avg `0.0147` n `8`; equity avg `0.0091` n `100`; fx avg `-0.0021` n `6`; index avg `0.0068` n `25`; metal avg `-0.0023` n `20`; unknown avg `0.0032` n `774`
- 1h: commodity avg `-0.0548` n `12`; crypto_alt avg `-0.0286` n `230`; crypto_major avg `-0.1447` n `8`; equity avg `0.0273` n `100`; fx avg `0.0267` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.0961` n `774`
- 4h: commodity avg `-0.046` n `12`; crypto_alt avg `0.2977` n `230`; crypto_major avg `0.565` n `8`; equity avg `0.207` n `100`; fx avg `-0.0015` n `6`; index avg `0.0519` n `25`; metal avg `0.0101` n `20`; unknown avg `-0.1204` n `774`
- 24h: commodity avg `-0.396` n `12`; crypto_alt avg `0.4955` n `230`; crypto_major avg `1.128` n `8`; equity avg `0.5487` n `100`; fx avg `-0.0064` n `6`; index avg `0.1473` n `25`; metal avg `0.0262` n `20`; unknown avg `-0.2978` n `757`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1325`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1202`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1189`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1146`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1117`, n `666`, weak_sample_signal
