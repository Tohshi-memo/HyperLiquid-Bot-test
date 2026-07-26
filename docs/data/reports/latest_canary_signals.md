# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T05:37:32.386414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `-0.0246` n `230`; crypto_major avg `-0.0506` n `8`; equity avg `-0.0361` n `100`; fx avg `-0.0039` n `6`; index avg `-0.0111` n `25`; metal avg `-0.0162` n `20`; unknown avg `0.4675` n `775`
- 1h: commodity avg `-0.0233` n `12`; crypto_alt avg `0.1127` n `230`; crypto_major avg `0.0459` n `8`; equity avg `-0.0625` n `100`; fx avg `-0.0038` n `6`; index avg `-0.0162` n `25`; metal avg `-0.0157` n `20`; unknown avg `-0.1138` n `775`
- 4h: commodity avg `-0.0555` n `12`; crypto_alt avg `0.4686` n `230`; crypto_major avg `0.4546` n `8`; equity avg `0.0048` n `100`; fx avg `0.0695` n `6`; index avg `0.0006` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.1599` n `774`
- 24h: commodity avg `-0.5362` n `12`; crypto_alt avg `1.1902` n `230`; crypto_major avg `1.6931` n `8`; equity avg `0.4456` n `100`; fx avg `0.0584` n `6`; index avg `0.115` n `25`; metal avg `0.0395` n `20`; unknown avg `-0.123` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1832`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1382`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1232`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1208`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1195`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1178`, n `666`, weak_sample_signal
