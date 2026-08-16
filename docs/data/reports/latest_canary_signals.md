# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T12:22:32.168435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.026` n `230`; crypto_major avg `-0.0081` n `8`; equity avg `-0.0074` n `114`; fx avg `0.0006` n `6`; index avg `0.0033` n `25`; metal avg `0.0019` n `20`; unknown avg `-0.0438` n `791`
- 1h: commodity avg `0.0041` n `12`; crypto_alt avg `0.0109` n `230`; crypto_major avg `-0.0225` n `8`; equity avg `0.0118` n `114`; fx avg `-0.0125` n `6`; index avg `0.0048` n `25`; metal avg `0.0089` n `20`; unknown avg `-0.0343` n `791`
- 4h: commodity avg `-0.0138` n `12`; crypto_alt avg `0.0597` n `230`; crypto_major avg `-0.1` n `8`; equity avg `-0.0477` n `114`; fx avg `-0.0088` n `6`; index avg `-0.0048` n `25`; metal avg `0.0196` n `20`; unknown avg `0.1108` n `791`
- 24h: commodity avg `0.0172` n `12`; crypto_alt avg `0.1524` n `230`; crypto_major avg `0.1566` n `8`; equity avg `0.3314` n `114`; fx avg `-0.0088` n `6`; index avg `0.0375` n `25`; metal avg `0.0332` n `20`; unknown avg `0.1131` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2143`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1762`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
