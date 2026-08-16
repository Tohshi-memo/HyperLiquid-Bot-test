# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T10:22:30.775661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.0655` n `230`; crypto_major avg `-0.0195` n `8`; equity avg `-0.0102` n `114`; fx avg `0.0002` n `6`; index avg `-0.0021` n `25`; metal avg `0.0015` n `20`; unknown avg `0.1562` n `791`
- 1h: commodity avg `-0.0146` n `12`; crypto_alt avg `-0.0264` n `230`; crypto_major avg `-0.1597` n `8`; equity avg `-0.017` n `114`; fx avg `-0.004` n `6`; index avg `-0.0129` n `25`; metal avg `0.0112` n `20`; unknown avg `0.151` n `791`
- 4h: commodity avg `-0.002` n `12`; crypto_alt avg `0.4582` n `230`; crypto_major avg `0.1358` n `8`; equity avg `0.0057` n `114`; fx avg `0.0009` n `6`; index avg `0.0034` n `25`; metal avg `0.0051` n `20`; unknown avg `0.1471` n `791`
- 24h: commodity avg `0.1137` n `12`; crypto_alt avg `-0.0266` n `230`; crypto_major avg `0.0683` n `8`; equity avg `0.3652` n `114`; fx avg `-0.0034` n `6`; index avg `0.0513` n `25`; metal avg `0.0372` n `20`; unknown avg `0.1292` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2067`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
