# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T20:01:10.987439+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `0.0014` n `230`; crypto_major avg `-0.0137` n `8`; equity avg `-0.0047` n `114`; fx avg `0.015` n `6`; index avg `-0.0017` n `25`; metal avg `0.0079` n `20`; unknown avg `0.0079` n `791`
- 1h: commodity avg `-0.0095` n `12`; crypto_alt avg `0.0442` n `230`; crypto_major avg `-0.0115` n `8`; equity avg `-0.0093` n `114`; fx avg `0.002` n `6`; index avg `0.0081` n `25`; metal avg `0.0073` n `20`; unknown avg `0.0807` n `791`
- 4h: commodity avg `0.0357` n `12`; crypto_alt avg `-0.2229` n `230`; crypto_major avg `-0.0817` n `8`; equity avg `0.0438` n `114`; fx avg `0.0016` n `6`; index avg `0.0119` n `25`; metal avg `0.0284` n `20`; unknown avg `-0.1222` n `791`
- 24h: commodity avg `0.0106` n `12`; crypto_alt avg `-0.3272` n `230`; crypto_major avg `-0.082` n `8`; equity avg `0.2669` n `114`; fx avg `0.0` n `6`; index avg `0.0367` n `25`; metal avg `0.0575` n `20`; unknown avg `0.1551` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2166`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
