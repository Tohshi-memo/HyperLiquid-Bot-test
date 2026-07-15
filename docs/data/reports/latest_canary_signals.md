# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T22:37:27.820982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0236` n `12`; crypto_alt avg `0.1401` n `230`; crypto_major avg `0.1174` n `8`; equity avg `-0.2353` n `94`; fx avg `-0.0016` n `6`; index avg `-0.0498` n `25`; metal avg `-0.016` n `20`; unknown avg `0.1649` n `768`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `0.1675` n `230`; crypto_major avg `0.1601` n `8`; equity avg `-0.1467` n `94`; fx avg `-0.0048` n `6`; index avg `-0.0166` n `25`; metal avg `0.0046` n `20`; unknown avg `0.3989` n `768`
- 4h: commodity avg `0.0393` n `12`; crypto_alt avg `-0.0467` n `230`; crypto_major avg `-0.3716` n `8`; equity avg `-0.3816` n `94`; fx avg `0.001` n `6`; index avg `-0.043` n `25`; metal avg `-0.0746` n `20`; unknown avg `-0.0627` n `768`
- 24h: commodity avg `0.1136` n `12`; crypto_alt avg `0.2395` n `230`; crypto_major avg `0.3492` n `8`; equity avg `-0.7502` n `93`; fx avg `0.2077` n `6`; index avg `-0.1664` n `25`; metal avg `0.17` n `20`; unknown avg `0.0913` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1488`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.123`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1152`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1141`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1127`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1097`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0929`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0852`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0848`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `669`, weak_sample_signal
