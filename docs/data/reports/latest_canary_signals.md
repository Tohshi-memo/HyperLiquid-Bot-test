# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T05:52:27.008651+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `0.0257` n `230`; crypto_major avg `-0.0317` n `8`; equity avg `0.0605` n `114`; fx avg `-0.001` n `6`; index avg `-0.0015` n `25`; metal avg `0.0042` n `20`; unknown avg `-0.022` n `791`
- 1h: commodity avg `-0.003` n `12`; crypto_alt avg `-0.0197` n `230`; crypto_major avg `-0.1312` n `8`; equity avg `0.0566` n `114`; fx avg `-0.0012` n `6`; index avg `0.0053` n `25`; metal avg `0.0199` n `20`; unknown avg `0.2845` n `791`
- 4h: commodity avg `-0.046` n `12`; crypto_alt avg `0.0529` n `230`; crypto_major avg `-0.0235` n `8`; equity avg `0.2196` n `114`; fx avg `-0.0039` n `6`; index avg `0.0133` n `25`; metal avg `0.0327` n `20`; unknown avg `0.0236` n `791`
- 24h: commodity avg `-0.0959` n `12`; crypto_alt avg `-0.2477` n `230`; crypto_major avg `-0.066` n `8`; equity avg `0.3855` n `114`; fx avg `-0.0164` n `6`; index avg `0.0493` n `25`; metal avg `0.0372` n `20`; unknown avg `-0.0131` n `765`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2197`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1832`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
