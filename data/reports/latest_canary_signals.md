# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T20:56:05.519389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `12`; crypto_alt avg `-0.2003` n `230`; crypto_major avg `-0.1174` n `8`; equity avg `0.0026` n `114`; fx avg `-0.0007` n `6`; index avg `-0.0118` n `25`; metal avg `0.0008` n `20`; unknown avg `0.339` n `791`
- 1h: commodity avg `0.018` n `12`; crypto_alt avg `-0.2345` n `230`; crypto_major avg `-0.1615` n `8`; equity avg `0.0069` n `114`; fx avg `0.0135` n `6`; index avg `-0.0098` n `25`; metal avg `-0.0291` n `20`; unknown avg `0.4062` n `791`
- 4h: commodity avg `0.0557` n `12`; crypto_alt avg `-0.3623` n `230`; crypto_major avg `-0.3205` n `8`; equity avg `0.0178` n `114`; fx avg `0.0025` n `6`; index avg `-0.0057` n `25`; metal avg `-0.0212` n `20`; unknown avg `0.1179` n `791`
- 24h: commodity avg `0.0581` n `12`; crypto_alt avg `-0.4272` n `230`; crypto_major avg `-0.1688` n `8`; equity avg `0.2751` n `114`; fx avg `-0.0003` n `6`; index avg `0.0446` n `25`; metal avg `0.0232` n `20`; unknown avg `0.1382` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2185`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
