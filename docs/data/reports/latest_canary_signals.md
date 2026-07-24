# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T13:52:29.345341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1914` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0687` n `12`; crypto_alt avg `-0.1307` n `230`; crypto_major avg `-0.2981` n `8`; equity avg `-1.1777` n `100`; fx avg `0.0062` n `6`; index avg `-0.1246` n `25`; metal avg `0.0176` n `20`; unknown avg `-0.1511` n `773`
- 1h: commodity avg `0.0051` n `12`; crypto_alt avg `-0.7486` n `230`; crypto_major avg `-0.8289` n `8`; equity avg `-2.012` n `100`; fx avg `0.008` n `6`; index avg `-0.2195` n `25`; metal avg `-0.095` n `20`; unknown avg `-0.2215` n `773`
- 4h: commodity avg `0.2593` n `12`; crypto_alt avg `-1.4947` n `230`; crypto_major avg `-1.4442` n `8`; equity avg `-2.2933` n `100`; fx avg `-0.0115` n `6`; index avg `-0.2528` n `25`; metal avg `-0.1352` n `20`; unknown avg `-0.276` n `773`
- 24h: commodity avg `-0.2902` n `12`; crypto_alt avg `-1.8778` n `230`; crypto_major avg `-1.9137` n `8`; equity avg `-2.9309` n `100`; fx avg `-0.1571` n `6`; index avg `-0.4363` n `25`; metal avg `-0.115` n `20`; unknown avg `0.1011` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.107`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1029`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0924`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
