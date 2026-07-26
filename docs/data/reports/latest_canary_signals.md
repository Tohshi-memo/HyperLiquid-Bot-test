# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T20:22:24.667403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0245` n `12`; crypto_alt avg `-0.0383` n `230`; crypto_major avg `-0.0569` n `8`; equity avg `0.0317` n `100`; fx avg `0.0078` n `6`; index avg `0.0043` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.1293` n `775`
- 1h: commodity avg `-0.0179` n `12`; crypto_alt avg `-0.0456` n `230`; crypto_major avg `-0.0404` n `8`; equity avg `-0.0471` n `100`; fx avg `0.0055` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0272` n `20`; unknown avg `-0.1043` n `775`
- 4h: commodity avg `0.2053` n `12`; crypto_alt avg `-0.2853` n `230`; crypto_major avg `-0.2374` n `8`; equity avg `-0.0298` n `100`; fx avg `0.0393` n `6`; index avg `-0.0326` n `25`; metal avg `0.0191` n `20`; unknown avg `-0.334` n `775`
- 24h: commodity avg `-0.2134` n `12`; crypto_alt avg `0.7697` n `230`; crypto_major avg `0.7995` n `8`; equity avg `0.6142` n `100`; fx avg `0.0461` n `6`; index avg `0.1023` n `25`; metal avg `0.1864` n `20`; unknown avg `-0.1102` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1921`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
