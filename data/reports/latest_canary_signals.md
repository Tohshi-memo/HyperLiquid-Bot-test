# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T01:22:18.434961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1585` n `12`; crypto_alt avg `0.0077` n `228`; crypto_major avg `0.1513` n `8`; equity avg `0.0944` n `67`; fx avg `0.0063` n `6`; index avg `0.0606` n `23`; metal avg `0.1401` n `18`; unknown avg `-0.1921` n `396`
- 1h: commodity avg `0.1065` n `12`; crypto_alt avg `0.353` n `228`; crypto_major avg `0.671` n `8`; equity avg `0.2517` n `67`; fx avg `-0.0005` n `6`; index avg `0.1455` n `23`; metal avg `0.1847` n `18`; unknown avg `-0.0864` n `396`
- 4h: commodity avg `0.5156` n `12`; crypto_alt avg `-0.6839` n `228`; crypto_major avg `-0.0405` n `8`; equity avg `0.2387` n `67`; fx avg `0.0305` n `6`; index avg `0.1146` n `23`; metal avg `0.2909` n `18`; unknown avg `-0.0194` n `396`
- 24h: commodity avg `-2.8356` n `12`; crypto_alt avg `2.6701` n `228`; crypto_major avg `2.7352` n `8`; equity avg `2.2642` n `67`; fx avg `0.0553` n `6`; index avg `1.145` n `23`; metal avg `1.2002` n `18`; unknown avg `1.6` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
