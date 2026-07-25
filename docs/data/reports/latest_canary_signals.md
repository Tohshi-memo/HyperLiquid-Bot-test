# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T01:37:32.316594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0143` n `12`; crypto_alt avg `0.0115` n `230`; crypto_major avg `0.1348` n `8`; equity avg `0.0287` n `100`; fx avg `-0.0071` n `6`; index avg `-0.0033` n `25`; metal avg `-0.0082` n `20`; unknown avg `0.0982` n `774`
- 1h: commodity avg `0.039` n `12`; crypto_alt avg `-0.0698` n `230`; crypto_major avg `-0.0538` n `8`; equity avg `0.0205` n `100`; fx avg `0.0051` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0261` n `20`; unknown avg `0.0685` n `774`
- 4h: commodity avg `-0.1166` n `12`; crypto_alt avg `0.0121` n `230`; crypto_major avg `0.1653` n `8`; equity avg `-0.0668` n `100`; fx avg `0.0403` n `6`; index avg `0.0015` n `25`; metal avg `-0.016` n `20`; unknown avg `-0.1892` n `774`
- 24h: commodity avg `-0.2326` n `12`; crypto_alt avg `-0.9837` n `230`; crypto_major avg `-0.9768` n `8`; equity avg `-3.0989` n `100`; fx avg `-0.0444` n `6`; index avg `-0.3699` n `25`; metal avg `0.0585` n `20`; unknown avg `14.006` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1237`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1163`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1083`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.107`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `666`, weak_sample_signal
