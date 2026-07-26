# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T20:52:28.084440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `-0.0526` n `230`; crypto_major avg `-0.007` n `8`; equity avg `0.0201` n `100`; fx avg `0.0` n `6`; index avg `-0.0001` n `25`; metal avg `0.0162` n `20`; unknown avg `-0.032` n `775`
- 1h: commodity avg `0.0128` n `12`; crypto_alt avg `-0.0975` n `230`; crypto_major avg `-0.0617` n `8`; equity avg `-0.0055` n `100`; fx avg `0.0029` n `6`; index avg `-0.0082` n `25`; metal avg `-0.017` n `20`; unknown avg `0.0648` n `775`
- 4h: commodity avg `0.2126` n `12`; crypto_alt avg `-0.3725` n `230`; crypto_major avg `-0.3434` n `8`; equity avg `-0.0684` n `100`; fx avg `0.0396` n `6`; index avg `-0.0512` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.279` n `775`
- 24h: commodity avg `-0.1942` n `12`; crypto_alt avg `0.7469` n `230`; crypto_major avg `0.781` n `8`; equity avg `0.598` n `100`; fx avg `0.0493` n `6`; index avg `0.0819` n `25`; metal avg `0.1872` n `20`; unknown avg `-0.0902` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1925`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1828`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
