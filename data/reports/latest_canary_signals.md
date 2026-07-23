# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T06:07:28.800828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `12`; crypto_alt avg `-0.0142` n `230`; crypto_major avg `0.0131` n `8`; equity avg `-0.081` n `98`; fx avg `0.0198` n `6`; index avg `-0.0208` n `25`; metal avg `-0.0577` n `20`; unknown avg `-0.0054` n `741`
- 1h: commodity avg `0.0386` n `12`; crypto_alt avg `-0.0199` n `230`; crypto_major avg `-0.0774` n `8`; equity avg `-0.0088` n `98`; fx avg `0.0061` n `6`; index avg `-0.0272` n `25`; metal avg `-0.0584` n `20`; unknown avg `0.0027` n `741`
- 4h: commodity avg `0.0764` n `12`; crypto_alt avg `-0.1139` n `230`; crypto_major avg `-0.2164` n `8`; equity avg `-0.1698` n `98`; fx avg `0.0338` n `6`; index avg `-0.0426` n `25`; metal avg `-0.0233` n `20`; unknown avg `-0.1727` n `741`
- 24h: commodity avg `0.793` n `12`; crypto_alt avg `-0.0397` n `230`; crypto_major avg `0.0448` n `8`; equity avg `0.4551` n `98`; fx avg `-0.1044` n `6`; index avg `0.1155` n `25`; metal avg `-0.1517` n `20`; unknown avg `1.6899` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0771`, n `666`, weak_sample_signal
