# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T13:52:26.429508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.013` n `12`; crypto_alt avg `0.0001` n `230`; crypto_major avg `0.066` n `8`; equity avg `-0.0009` n `100`; fx avg `0.0008` n `6`; index avg `0.0023` n `25`; metal avg `0.0019` n `20`; unknown avg `-0.0048` n `775`
- 1h: commodity avg `0.0568` n `12`; crypto_alt avg `-0.1868` n `230`; crypto_major avg `-0.054` n `8`; equity avg `0.0446` n `100`; fx avg `-0.0036` n `6`; index avg `0.0064` n `25`; metal avg `0.0029` n `20`; unknown avg `-0.0581` n `775`
- 4h: commodity avg `-0.1306` n `12`; crypto_alt avg `-0.1185` n `230`; crypto_major avg `-0.0918` n `8`; equity avg `0.2045` n `100`; fx avg `0.006` n `6`; index avg `0.0382` n `25`; metal avg `0.0748` n `20`; unknown avg `-0.082` n `775`
- 24h: commodity avg `-0.4101` n `12`; crypto_alt avg `1.1395` n `230`; crypto_major avg `1.3561` n `8`; equity avg `0.8051` n `100`; fx avg `0.0218` n `6`; index avg `0.1643` n `25`; metal avg `0.1799` n `20`; unknown avg `0.0318` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1899`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
