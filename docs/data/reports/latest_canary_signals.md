# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T19:37:26.668329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `0.0251` n `230`; crypto_major avg `0.0294` n `8`; equity avg `0.0089` n `114`; fx avg `0.0046` n `6`; index avg `-0.0063` n `25`; metal avg `-0.0017` n `20`; unknown avg `-0.0625` n `791`
- 1h: commodity avg `0.0334` n `12`; crypto_alt avg `0.0269` n `230`; crypto_major avg `0.0842` n `8`; equity avg `0.0482` n `114`; fx avg `0.0068` n `6`; index avg `0.0026` n `25`; metal avg `0.0002` n `20`; unknown avg `0.0092` n `791`
- 4h: commodity avg `0.0906` n `12`; crypto_alt avg `-0.0667` n `230`; crypto_major avg `0.0593` n `8`; equity avg `0.0738` n `114`; fx avg `0.0049` n `6`; index avg `0.005` n `25`; metal avg `0.0` n `20`; unknown avg `-0.0167` n `791`
- 24h: commodity avg `-0.0004` n `12`; crypto_alt avg `1.0453` n `230`; crypto_major avg `0.6957` n `8`; equity avg `0.3681` n `114`; fx avg `0.0278` n `6`; index avg `0.0263` n `25`; metal avg `0.0172` n `20`; unknown avg `0.1532` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1824`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
