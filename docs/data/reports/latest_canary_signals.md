# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T11:37:23.933051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0507` n `12`; crypto_alt avg `0.039` n `230`; crypto_major avg `0.0013` n `8`; equity avg `0.0226` n `100`; fx avg `0.0` n `6`; index avg `0.005` n `25`; metal avg `-0.0188` n `20`; unknown avg `-0.0057` n `775`
- 1h: commodity avg `-0.0423` n `12`; crypto_alt avg `0.0008` n `230`; crypto_major avg `-0.0405` n `8`; equity avg `0.066` n `100`; fx avg `-0.004` n `6`; index avg `-0.013` n `25`; metal avg `0.0254` n `20`; unknown avg `0.0092` n `775`
- 4h: commodity avg `-0.3496` n `12`; crypto_alt avg `-0.0062` n `230`; crypto_major avg `0.1139` n `8`; equity avg `0.2308` n `100`; fx avg `-0.0361` n `6`; index avg `0.0481` n `25`; metal avg `0.1229` n `20`; unknown avg `-0.0049` n `775`
- 24h: commodity avg `-0.9005` n `12`; crypto_alt avg `1.769` n `230`; crypto_major avg `1.7522` n `8`; equity avg `0.8657` n `100`; fx avg `0.0136` n `6`; index avg `0.1733` n `25`; metal avg `0.1792` n `20`; unknown avg `0.1482` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1903`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1473`, n `667`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1353`, n `667`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1319`, n `667`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.126`, n `667`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1249`, n `667`, weak_sample_signal
