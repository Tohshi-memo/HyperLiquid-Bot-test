# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T16:07:32.998308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `-0.0558` n `230`; crypto_major avg `-0.0254` n `8`; equity avg `0.0025` n `114`; fx avg `-0.0006` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0018` n `20`; unknown avg `-0.0118` n `791`
- 1h: commodity avg `0.0084` n `12`; crypto_alt avg `0.1357` n `230`; crypto_major avg `0.1157` n `8`; equity avg `0.0033` n `114`; fx avg `-0.0007` n `6`; index avg `0.0034` n `25`; metal avg `0.0019` n `20`; unknown avg `5.6116` n `791`
- 4h: commodity avg `-0.041` n `12`; crypto_alt avg `0.3467` n `230`; crypto_major avg `0.235` n `8`; equity avg `0.0481` n `114`; fx avg `-0.0049` n `6`; index avg `0.0192` n `25`; metal avg `-0.0088` n `20`; unknown avg `-0.0321` n `791`
- 24h: commodity avg `-0.0562` n `12`; crypto_alt avg `1.0803` n `230`; crypto_major avg `0.3447` n `8`; equity avg `0.2932` n `114`; fx avg `0.0076` n `6`; index avg `0.0402` n `25`; metal avg `-0.0188` n `20`; unknown avg `0.0038` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1851`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.178`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
