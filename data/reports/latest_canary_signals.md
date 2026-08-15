# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T12:37:25.293198+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `12`; crypto_alt avg `-0.0394` n `230`; crypto_major avg `0.0051` n `8`; equity avg `-0.0041` n `114`; fx avg `0.0033` n `6`; index avg `0.002` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.0012` n `791`
- 1h: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.1115` n `230`; crypto_major avg `-0.0093` n `8`; equity avg `0.0134` n `114`; fx avg `0.0016` n `6`; index avg `0.0201` n `25`; metal avg `-0.0094` n `20`; unknown avg `-0.0471` n `791`
- 4h: commodity avg `0.0501` n `12`; crypto_alt avg `-0.1156` n `230`; crypto_major avg `-0.046` n `8`; equity avg `-0.0017` n `114`; fx avg `-0.0069` n `6`; index avg `0.0172` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.0412` n `791`
- 24h: commodity avg `0.0659` n `12`; crypto_alt avg `1.1107` n `230`; crypto_major avg `0.1808` n `8`; equity avg `-0.6887` n `114`; fx avg `0.1547` n `6`; index avg `-0.1333` n `25`; metal avg `0.0756` n `20`; unknown avg `-0.1523` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
