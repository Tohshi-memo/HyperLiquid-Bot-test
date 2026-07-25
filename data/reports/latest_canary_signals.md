# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T04:07:26.563419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0207` n `12`; crypto_alt avg `0.0899` n `230`; crypto_major avg `0.0501` n `8`; equity avg `0.0313` n `100`; fx avg `-0.0014` n `6`; index avg `-0.0013` n `25`; metal avg `-0.0019` n `20`; unknown avg `-0.0966` n `774`
- 1h: commodity avg `-0.0333` n `12`; crypto_alt avg `0.0122` n `230`; crypto_major avg `-0.0068` n `8`; equity avg `0.0156` n `100`; fx avg `-0.0037` n `6`; index avg `-0.0064` n `25`; metal avg `-0.0082` n `20`; unknown avg `0.2607` n `774`
- 4h: commodity avg `-0.1643` n `12`; crypto_alt avg `0.0059` n `230`; crypto_major avg `0.03` n `8`; equity avg `0.1606` n `100`; fx avg `-0.0522` n `6`; index avg `0.0084` n `25`; metal avg `-0.0315` n `20`; unknown avg `1.1664` n `774`
- 24h: commodity avg `-0.4963` n `12`; crypto_alt avg `-1.2035` n `230`; crypto_major avg `-1.0793` n `8`; equity avg `-2.1624` n `100`; fx avg `-0.0415` n `6`; index avg `-0.1424` n `25`; metal avg `0.1765` n `20`; unknown avg `13.845` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1155`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1078`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1024`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
