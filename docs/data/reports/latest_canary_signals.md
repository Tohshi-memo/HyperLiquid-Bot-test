# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T18:52:27.661840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `0.0096` n `230`; crypto_major avg `-0.0118` n `8`; equity avg `0.0047` n `114`; fx avg `0.0001` n `6`; index avg `-0.002` n `25`; metal avg `-0.0003` n `20`; unknown avg `0.0872` n `791`
- 1h: commodity avg `0.0232` n `12`; crypto_alt avg `-0.1174` n `230`; crypto_major avg `-0.0928` n `8`; equity avg `0.023` n `114`; fx avg `-0.0041` n `6`; index avg `-0.0075` n `25`; metal avg `0.004` n `20`; unknown avg `0.4442` n `791`
- 4h: commodity avg `0.0565` n `12`; crypto_alt avg `0.09` n `230`; crypto_major avg `0.0948` n `8`; equity avg `0.0648` n `114`; fx avg `-0.0024` n `6`; index avg `0.0064` n `25`; metal avg `-0.0007` n `20`; unknown avg `5.6833` n `791`
- 24h: commodity avg `-0.0733` n `12`; crypto_alt avg `0.9931` n `230`; crypto_major avg `0.598` n `8`; equity avg `0.317` n `114`; fx avg `0.0217` n `6`; index avg `0.0209` n `25`; metal avg `0.0478` n `20`; unknown avg `0.0791` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
