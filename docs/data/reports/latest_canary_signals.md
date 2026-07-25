# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T16:37:24.819992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0017` n `12`; crypto_alt avg `0.0866` n `230`; crypto_major avg `0.1431` n `8`; equity avg `0.0377` n `100`; fx avg `-0.0179` n `6`; index avg `-0.0133` n `25`; metal avg `-0.0078` n `20`; unknown avg `0.0201` n `774`
- 1h: commodity avg `0.0512` n `12`; crypto_alt avg `0.097` n `230`; crypto_major avg `0.1703` n `8`; equity avg `0.0092` n `100`; fx avg `-0.0229` n `6`; index avg `-0.0155` n `25`; metal avg `-0.0188` n `20`; unknown avg `0.0233` n `774`
- 4h: commodity avg `-0.3458` n `12`; crypto_alt avg `0.6226` n `230`; crypto_major avg `0.8269` n `8`; equity avg `0.0227` n `100`; fx avg `-0.0196` n `6`; index avg `-0.0029` n `25`; metal avg `0.0038` n `20`; unknown avg `0.0566` n `774`
- 24h: commodity avg `-0.224` n `12`; crypto_alt avg `0.278` n `230`; crypto_major avg `0.7975` n `8`; equity avg `-1.1175` n `100`; fx avg `-0.0494` n `6`; index avg `-0.1591` n `25`; metal avg `-0.1875` n `20`; unknown avg `-0.3468` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1265`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1157`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1105`, n `666`, weak_sample_signal
