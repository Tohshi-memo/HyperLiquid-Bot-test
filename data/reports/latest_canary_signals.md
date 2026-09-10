# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T19:37:33.008303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0212` n `12`; crypto_alt avg `-0.0331` n `233`; crypto_major avg `-0.0254` n `8`; equity avg `-0.062` n `135`; fx avg `-0.0001` n `6`; index avg `0.0093` n `26`; metal avg `0.0017` n `20`; unknown avg `8.3137` n `797`
- 1h: commodity avg `0.0814` n `12`; crypto_alt avg `0.1133` n `233`; crypto_major avg `0.2457` n `8`; equity avg `-0.1574` n `135`; fx avg `0.0186` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0276` n `20`; unknown avg `8.9308` n `795`
- 4h: commodity avg `0.4475` n `12`; crypto_alt avg `-0.2572` n `233`; crypto_major avg `-0.0183` n `8`; equity avg `-0.8413` n `135`; fx avg `0.0339` n `6`; index avg `-0.1117` n `26`; metal avg `-0.3115` n `20`; unknown avg `-0.0665` n `788`
- 24h: commodity avg `1.0697` n `12`; crypto_alt avg `-3.6494` n `233`; crypto_major avg `-2.895` n `8`; equity avg `-2.1598` n `135`; fx avg `0.1152` n `6`; index avg `-0.3536` n `26`; metal avg `-1.2411` n `20`; unknown avg `-0.5307` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
