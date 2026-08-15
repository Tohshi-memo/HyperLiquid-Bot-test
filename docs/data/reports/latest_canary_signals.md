# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T23:22:28.414640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `-0.1803` n `230`; crypto_major avg `-0.1136` n `8`; equity avg `0.0013` n `114`; fx avg `-0.0034` n `6`; index avg `0.0068` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.0903` n `791`
- 1h: commodity avg `0.0315` n `12`; crypto_alt avg `-0.3944` n `230`; crypto_major avg `-0.2228` n `8`; equity avg `0.013` n `114`; fx avg `-0.0029` n `6`; index avg `0.0156` n `25`; metal avg `-0.0074` n `20`; unknown avg `0.1103` n `791`
- 4h: commodity avg `-0.0225` n `12`; crypto_alt avg `-0.3789` n `230`; crypto_major avg `-0.1818` n `8`; equity avg `0.0021` n `114`; fx avg `-0.0029` n `6`; index avg `-0.0035` n `25`; metal avg `-0.007` n `20`; unknown avg `0.062` n `791`
- 24h: commodity avg `-0.0613` n `12`; crypto_alt avg `0.332` n `230`; crypto_major avg `0.2638` n `8`; equity avg `0.1341` n `114`; fx avg `0.0086` n `6`; index avg `0.0078` n `25`; metal avg `0.0012` n `20`; unknown avg `0.1503` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1824`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
