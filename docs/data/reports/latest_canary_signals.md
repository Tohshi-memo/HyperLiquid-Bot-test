# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T16:36:49.136956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0127` n `12`; crypto_alt avg `-0.0778` n `230`; crypto_major avg `-0.0793` n `8`; equity avg `-0.022` n `114`; fx avg `-0.0012` n `6`; index avg `0.0017` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.0645` n `791`
- 1h: commodity avg `0.0179` n `12`; crypto_alt avg `-0.0445` n `230`; crypto_major avg `-0.0352` n `8`; equity avg `-0.0309` n `114`; fx avg `-0.0007` n `6`; index avg `0.0011` n `25`; metal avg `-0.007` n `20`; unknown avg `0.0034` n `791`
- 4h: commodity avg `-0.0288` n `12`; crypto_alt avg `0.4721` n `230`; crypto_major avg `0.2456` n `8`; equity avg `0.033` n `114`; fx avg `-0.0061` n `6`; index avg `0.0035` n `25`; metal avg `-0.0137` n `20`; unknown avg `-0.1166` n `791`
- 24h: commodity avg `-0.0711` n `12`; crypto_alt avg `0.6972` n `230`; crypto_major avg `0.1513` n `8`; equity avg `0.1986` n `114`; fx avg `0.0051` n `6`; index avg `0.033` n `25`; metal avg `-0.0221` n `20`; unknown avg `-0.0163` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.178`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
