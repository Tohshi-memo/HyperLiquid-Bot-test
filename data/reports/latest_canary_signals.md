# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T19:52:30.631834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0188` n `12`; crypto_alt avg `-0.038` n `230`; crypto_major avg `0.0106` n `8`; equity avg `-0.0117` n `100`; fx avg `0.002` n `6`; index avg `0.0008` n `25`; metal avg `-0.0066` n `20`; unknown avg `-0.0721` n `775`
- 1h: commodity avg `0.1024` n `12`; crypto_alt avg `-0.0797` n `230`; crypto_major avg `-0.1069` n `8`; equity avg `-0.0869` n `100`; fx avg `0.0202` n `6`; index avg `-0.0208` n `25`; metal avg `0.0066` n `20`; unknown avg `-0.2062` n `775`
- 4h: commodity avg `0.2079` n `12`; crypto_alt avg `-0.1923` n `230`; crypto_major avg `-0.1106` n `8`; equity avg `-0.0168` n `100`; fx avg `0.0376` n `6`; index avg `-0.0124` n `25`; metal avg `0.0696` n `20`; unknown avg `-0.4053` n `775`
- 24h: commodity avg `-0.2129` n `12`; crypto_alt avg `0.7209` n `230`; crypto_major avg `0.7084` n `8`; equity avg `0.6262` n `100`; fx avg `0.0488` n `6`; index avg `0.1134` n `25`; metal avg `0.2068` n `20`; unknown avg `-0.1118` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
