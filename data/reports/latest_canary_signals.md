# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T12:02:06.273703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.0003` n `230`; crypto_major avg `-0.0545` n `8`; equity avg `-0.0232` n `99`; fx avg `-0.0004` n `6`; index avg `0.0137` n `25`; metal avg `-0.0082` n `20`; unknown avg `-0.0122` n `772`
- 1h: commodity avg `-0.0205` n `12`; crypto_alt avg `0.0491` n `230`; crypto_major avg `-0.0632` n `8`; equity avg `-0.3764` n `99`; fx avg `0.009` n `6`; index avg `-0.088` n `25`; metal avg `-0.0531` n `20`; unknown avg `0.0229` n `772`
- 4h: commodity avg `0.1668` n `12`; crypto_alt avg `0.1333` n `230`; crypto_major avg `0.2182` n `8`; equity avg `-0.1785` n `99`; fx avg `-0.0228` n `6`; index avg `-0.0549` n `25`; metal avg `-0.1527` n `20`; unknown avg `0.0147` n `772`
- 24h: commodity avg `0.6749` n `12`; crypto_alt avg `-0.1647` n `230`; crypto_major avg `0.108` n `8`; equity avg `0.6504` n `99`; fx avg `-0.0871` n `6`; index avg `0.1554` n `25`; metal avg `-0.4967` n `20`; unknown avg `10.1896` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0728`, n `666`, weak_sample_signal
