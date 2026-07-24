# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T14:37:24.837955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0834` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `0.0087` n `230`; crypto_major avg `0.179` n `8`; equity avg `-0.4518` n `100`; fx avg `-0.0031` n `6`; index avg `-0.0405` n `25`; metal avg `0.014` n `20`; unknown avg `0.0495` n `773`
- 1h: commodity avg `-0.0696` n `12`; crypto_alt avg `-0.3358` n `230`; crypto_major avg `-0.3856` n `8`; equity avg `-1.7289` n `100`; fx avg `0.0055` n `6`; index avg `-0.1554` n `25`; metal avg `0.0225` n `20`; unknown avg `-0.1624` n `773`
- 4h: commodity avg `0.0804` n `12`; crypto_alt avg `-1.3451` n `230`; crypto_major avg `-1.3472` n `8`; equity avg `-2.6631` n `100`; fx avg `-0.0095` n `6`; index avg `-0.2638` n `25`; metal avg `-0.124` n `20`; unknown avg `-0.171` n `773`
- 24h: commodity avg `-0.3026` n `12`; crypto_alt avg `-2.4117` n `230`; crypto_major avg `-2.2647` n `8`; equity avg `-3.6216` n `100`; fx avg `-0.1431` n `6`; index avg `-0.4529` n `25`; metal avg `-0.105` n `20`; unknown avg `0.0749` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1225`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1165`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1118`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1013`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1004`, n `666`, weak_sample_signal
