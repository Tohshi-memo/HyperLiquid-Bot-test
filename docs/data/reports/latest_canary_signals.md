# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T08:52:29.924912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `-0.0874` n `230`; crypto_major avg `0.0506` n `8`; equity avg `0.0387` n `100`; fx avg `-0.0044` n `6`; index avg `-0.0028` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.0445` n `775`
- 1h: commodity avg `-0.0418` n `12`; crypto_alt avg `-0.005` n `230`; crypto_major avg `0.0738` n `8`; equity avg `-0.0237` n `100`; fx avg `-0.0427` n `6`; index avg `-0.0017` n `25`; metal avg `0.0116` n `20`; unknown avg `-0.004` n `775`
- 4h: commodity avg `-0.047` n `12`; crypto_alt avg `0.2422` n `230`; crypto_major avg `-0.0422` n `8`; equity avg `-0.0742` n `100`; fx avg `-0.0445` n `6`; index avg `-0.0042` n `25`; metal avg `0.0215` n `20`; unknown avg `-0.0392` n `759`
- 24h: commodity avg `-0.6226` n `12`; crypto_alt avg `1.8453` n `230`; crypto_major avg `1.9246` n `8`; equity avg `0.5382` n `100`; fx avg `-0.0152` n `6`; index avg `0.131` n `25`; metal avg `0.0774` n `20`; unknown avg `0.0795` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1439`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1285`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1275`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1233`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1207`, n `666`, weak_sample_signal
