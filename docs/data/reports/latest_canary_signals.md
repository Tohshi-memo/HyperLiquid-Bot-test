# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T21:52:25.529825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0179` n `12`; crypto_alt avg `-0.153` n `230`; crypto_major avg `-0.1439` n `8`; equity avg `-0.0323` n `100`; fx avg `0.0118` n `6`; index avg `-0.0061` n `25`; metal avg `0.0001` n `20`; unknown avg `-0.0631` n `774`
- 1h: commodity avg `0.0464` n `12`; crypto_alt avg `-0.1444` n `230`; crypto_major avg `-0.2801` n `8`; equity avg `-0.0314` n `100`; fx avg `0.004` n `6`; index avg `0.0104` n `25`; metal avg `0.0047` n `20`; unknown avg `-0.1078` n `774`
- 4h: commodity avg `0.396` n `12`; crypto_alt avg `-0.4304` n `230`; crypto_major avg `-0.4337` n `8`; equity avg `-0.927` n `100`; fx avg `-0.0038` n `6`; index avg `-0.1532` n `25`; metal avg `-0.106` n `20`; unknown avg `-0.043` n `773`
- 24h: commodity avg `-0.2568` n `12`; crypto_alt avg `-1.1828` n `230`; crypto_major avg `-1.2569` n `8`; equity avg `-3.3048` n `100`; fx avg `-0.1619` n `6`; index avg `-0.4918` n `25`; metal avg `-0.0394` n `20`; unknown avg `14.0023` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1269`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1216`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1117`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1101`, n `666`, weak_sample_signal
