# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T12:07:26.381129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0258` n `12`; crypto_alt avg `0.0888` n `230`; crypto_major avg `0.1758` n `8`; equity avg `-0.0366` n `100`; fx avg `0.0045` n `6`; index avg `-0.0057` n `25`; metal avg `0.0102` n `20`; unknown avg `0.029` n `775`
- 1h: commodity avg `-0.0137` n `12`; crypto_alt avg `0.1274` n `230`; crypto_major avg `0.1099` n `8`; equity avg `0.0106` n `100`; fx avg `-0.0005` n `6`; index avg `-0.0079` n `25`; metal avg `0.0009` n `20`; unknown avg `0.0235` n `775`
- 4h: commodity avg `-0.306` n `12`; crypto_alt avg `0.0458` n `230`; crypto_major avg `0.2755` n `8`; equity avg `0.2265` n `100`; fx avg `0.0016` n `6`; index avg `0.0512` n `25`; metal avg `0.1223` n `20`; unknown avg `-0.0522` n `775`
- 24h: commodity avg `-0.8166` n `12`; crypto_alt avg `1.7191` n `230`; crypto_major avg `1.7513` n `8`; equity avg `0.7335` n `100`; fx avg `0.0211` n `6`; index avg `0.1698` n `25`; metal avg `0.198` n `20`; unknown avg `0.1229` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
