# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T04:07:28.531530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0277` n `12`; crypto_alt avg `0.0051` n `230`; crypto_major avg `0.0323` n `8`; equity avg `0.0276` n `113`; fx avg `0.0033` n `6`; index avg `0.0126` n `25`; metal avg `0.0088` n `20`; unknown avg `0.0228` n `785`
- 1h: commodity avg `-0.0581` n `12`; crypto_alt avg `0.0066` n `230`; crypto_major avg `0.0355` n `8`; equity avg `0.1496` n `113`; fx avg `0.0054` n `6`; index avg `0.0347` n `25`; metal avg `0.0279` n `20`; unknown avg `1.6889` n `785`
- 4h: commodity avg `-0.0356` n `12`; crypto_alt avg `0.243` n `230`; crypto_major avg `0.4049` n `8`; equity avg `0.762` n `113`; fx avg `-0.0459` n `6`; index avg `0.2282` n `25`; metal avg `0.0662` n `20`; unknown avg `-0.1182` n `785`
- 24h: commodity avg `0.7501` n `12`; crypto_alt avg `-0.4559` n `230`; crypto_major avg `-0.3997` n `8`; equity avg `-0.8715` n `113`; fx avg `0.1294` n `6`; index avg `0.0631` n `25`; metal avg `0.5602` n `20`; unknown avg `103.9033` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1578`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1566`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1564`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1549`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1545`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1406`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1238`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.119`, n `669`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1073`, n `669`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0951`, n `669`, weak_sample_signal
