# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T12:22:27.679163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.027` n `12`; crypto_alt avg `-0.1081` n `230`; crypto_major avg `-0.1098` n `8`; equity avg `-0.0182` n `100`; fx avg `0.0031` n `6`; index avg `-0.0069` n `25`; metal avg `-0.0164` n `20`; unknown avg `-0.0068` n `775`
- 1h: commodity avg `-0.0254` n `12`; crypto_alt avg `-0.0341` n `230`; crypto_major avg `-0.0304` n `8`; equity avg `-0.0145` n `100`; fx avg `0.009` n `6`; index avg `-0.0026` n `25`; metal avg `-0.0236` n `20`; unknown avg `-0.0974` n `775`
- 4h: commodity avg `-0.3138` n `12`; crypto_alt avg `-0.1105` n `230`; crypto_major avg `0.127` n `8`; equity avg `0.2232` n `100`; fx avg `0.0059` n `6`; index avg `0.0393` n `25`; metal avg `0.0956` n `20`; unknown avg `-0.0694` n `775`
- 24h: commodity avg `-0.8486` n `12`; crypto_alt avg `1.6039` n `230`; crypto_major avg `1.7035` n `8`; equity avg `0.736` n `100`; fx avg `0.0267` n `6`; index avg `0.1672` n `25`; metal avg `0.179` n `20`; unknown avg `0.108` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1902`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.178`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
