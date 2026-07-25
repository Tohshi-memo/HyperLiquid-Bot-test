# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T00:22:28.767361+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0438` n `12`; crypto_alt avg `0.0494` n `230`; crypto_major avg `0.0144` n `8`; equity avg `-0.0534` n `100`; fx avg `-0.0407` n `6`; index avg `-0.0115` n `25`; metal avg `0.0003` n `20`; unknown avg `0.2562` n `774`
- 1h: commodity avg `-0.1028` n `12`; crypto_alt avg `0.0809` n `230`; crypto_major avg `0.0753` n `8`; equity avg `0.0895` n `100`; fx avg `-0.0209` n `6`; index avg `0.0345` n `25`; metal avg `0.0044` n `20`; unknown avg `-0.0877` n `774`
- 4h: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.1144` n `230`; crypto_major avg `-0.1312` n `8`; equity avg `-0.1562` n `100`; fx avg `0.0088` n `6`; index avg `0.0092` n `25`; metal avg `0.0272` n `20`; unknown avg `-0.1949` n `774`
- 24h: commodity avg `-0.4402` n `12`; crypto_alt avg `-0.6474` n `230`; crypto_major avg `-0.6704` n `8`; equity avg `-2.988` n `100`; fx avg `-0.1305` n `6`; index avg `-0.3505` n `25`; metal avg `0.0442` n `20`; unknown avg `13.9656` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1274`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.12`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1108`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1103`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
