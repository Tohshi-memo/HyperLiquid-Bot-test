# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T02:52:24.534873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.06` n `12`; crypto_alt avg `-0.0412` n `230`; crypto_major avg `-0.0581` n `8`; equity avg `0.0628` n `100`; fx avg `0.002` n `6`; index avg `0.0231` n `25`; metal avg `0.0004` n `20`; unknown avg `0.0876` n `774`
- 1h: commodity avg `-0.1258` n `12`; crypto_alt avg `-0.0915` n `230`; crypto_major avg `-0.0852` n `8`; equity avg `0.1201` n `100`; fx avg `-0.0292` n `6`; index avg `0.027` n `25`; metal avg `-0.0046` n `20`; unknown avg `-0.104` n `774`
- 4h: commodity avg `-0.1403` n `12`; crypto_alt avg `-0.0559` n `230`; crypto_major avg `0.0277` n `8`; equity avg `0.0466` n `100`; fx avg `0.0073` n `6`; index avg `0.044` n `25`; metal avg `-0.0256` n `20`; unknown avg `-0.1339` n `774`
- 24h: commodity avg `-0.4375` n `12`; crypto_alt avg `-0.8924` n `230`; crypto_major avg `-0.6778` n `8`; equity avg `-2.3854` n `100`; fx avg `-0.0464` n `6`; index avg `-0.1318` n `25`; metal avg `0.2585` n `20`; unknown avg `14.0362` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1206`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1131`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1053`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1048`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.103`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
