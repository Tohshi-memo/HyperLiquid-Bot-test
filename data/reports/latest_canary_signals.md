# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T19:07:25.675626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0778` n `12`; crypto_alt avg `-0.0513` n `230`; crypto_major avg `-0.1004` n `8`; equity avg `-0.0371` n `100`; fx avg `-0.0046` n `6`; index avg `-0.0179` n `25`; metal avg `0.0131` n `20`; unknown avg `0.0234` n `775`
- 1h: commodity avg `0.1615` n `12`; crypto_alt avg `-0.0399` n `230`; crypto_major avg `-0.0208` n `8`; equity avg `-0.0033` n `100`; fx avg `-0.0013` n `6`; index avg `-0.0307` n `25`; metal avg `0.022` n `20`; unknown avg `-0.1773` n `775`
- 4h: commodity avg `0.2057` n `12`; crypto_alt avg `0.1595` n `230`; crypto_major avg `0.0973` n `8`; equity avg `0.066` n `100`; fx avg `-0.0002` n `6`; index avg `-0.0129` n `25`; metal avg `0.0543` n `20`; unknown avg `-0.2299` n `775`
- 24h: commodity avg `-0.2446` n `12`; crypto_alt avg `0.7026` n `230`; crypto_major avg `0.6032` n `8`; equity avg `0.7182` n `100`; fx avg `0.0302` n `6`; index avg `0.1294` n `25`; metal avg `0.2038` n `20`; unknown avg `-0.0777` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1922`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
