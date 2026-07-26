# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T04:37:26.669955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `12`; crypto_alt avg `0.0715` n `230`; crypto_major avg `0.1334` n `8`; equity avg `0.0004` n `100`; fx avg `-0.0022` n `6`; index avg `-0.0013` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.0903` n `775`
- 1h: commodity avg `-0.0337` n `12`; crypto_alt avg `0.0525` n `230`; crypto_major avg `0.1216` n `8`; equity avg `0.0099` n `100`; fx avg `0.0592` n `6`; index avg `0.0096` n `25`; metal avg `0.0138` n `20`; unknown avg `-0.1183` n `775`
- 4h: commodity avg `-0.0353` n `12`; crypto_alt avg `0.4637` n `230`; crypto_major avg `0.4894` n `8`; equity avg `0.2294` n `100`; fx avg `0.0614` n `6`; index avg `0.0318` n `25`; metal avg `0.0213` n `20`; unknown avg `-0.1302` n `774`
- 24h: commodity avg `-0.518` n `12`; crypto_alt avg `0.8782` n `230`; crypto_major avg `1.4789` n `8`; equity avg `0.4732` n `100`; fx avg `0.071` n `6`; index avg `0.1361` n `25`; metal avg `0.0577` n `20`; unknown avg `-0.2104` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1834`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1375`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1244`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1177`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1165`, n `666`, weak_sample_signal
