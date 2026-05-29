# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T05:22:22.418625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0583` n `12`; crypto_alt avg `-0.1363` n `228`; crypto_major avg `-0.0542` n `8`; equity avg `0.0296` n `69`; fx avg `0.0101` n `6`; index avg `-0.036` n `23`; metal avg `0.0017` n `18`; unknown avg `0.0195` n `417`
- 1h: commodity avg `0.017` n `12`; crypto_alt avg `0.4776` n `228`; crypto_major avg `0.4878` n `8`; equity avg `0.2934` n `69`; fx avg `0.0334` n `6`; index avg `0.0639` n `23`; metal avg `0.1328` n `18`; unknown avg `0.2015` n `417`
- 4h: commodity avg `-0.1619` n `12`; crypto_alt avg `-0.17` n `228`; crypto_major avg `-0.0166` n `8`; equity avg `0.5198` n `69`; fx avg `0.0061` n `6`; index avg `0.14` n `23`; metal avg `-0.3492` n `18`; unknown avg `-0.7027` n `417`
- 24h: commodity avg `-0.2789` n `12`; crypto_alt avg `1.7567` n `228`; crypto_major avg `2.2786` n `8`; equity avg `4.6366` n `69`; fx avg `0.1744` n `6`; index avg `1.6638` n `23`; metal avg `2.7902` n `18`; unknown avg `1.0004` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
