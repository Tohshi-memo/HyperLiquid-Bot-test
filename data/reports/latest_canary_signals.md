# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T00:37:32.508102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0207` n `12`; crypto_alt avg `0.0003` n `230`; crypto_major avg `-0.0492` n `8`; equity avg `-0.0395` n `100`; fx avg `0.0123` n `6`; index avg `-0.002` n `25`; metal avg `0.0001` n `20`; unknown avg `0.0513` n `774`
- 1h: commodity avg `0.0003` n `12`; crypto_alt avg `0.0367` n `230`; crypto_major avg `0.0788` n `8`; equity avg `0.0017` n `100`; fx avg `0.0021` n `6`; index avg `0.0164` n `25`; metal avg `0.0126` n `20`; unknown avg `-0.1539` n `774`
- 4h: commodity avg `-0.0238` n `12`; crypto_alt avg `0.0092` n `230`; crypto_major avg `0.0569` n `8`; equity avg `0.0823` n `100`; fx avg `-0.0002` n `6`; index avg `0.017` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.2619` n `774`
- 24h: commodity avg `-0.5669` n `12`; crypto_alt avg `0.3377` n `230`; crypto_major avg `0.96` n `8`; equity avg `0.4732` n `100`; fx avg `-0.0182` n `6`; index avg `0.1471` n `25`; metal avg `0.0051` n `20`; unknown avg `-0.2568` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1351`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1234`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1168`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1155`, n `666`, weak_sample_signal
