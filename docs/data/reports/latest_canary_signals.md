# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T00:22:32.908665+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `12`; crypto_alt avg `0.0533` n `230`; crypto_major avg `0.006` n `8`; equity avg `0.0002` n `114`; fx avg `0.0059` n `6`; index avg `-0.001` n `25`; metal avg `0.0041` n `20`; unknown avg `-0.0098` n `791`
- 1h: commodity avg `-0.0135` n `12`; crypto_alt avg `0.017` n `230`; crypto_major avg `-0.0417` n `8`; equity avg `0.0108` n `114`; fx avg `0.0057` n `6`; index avg `-0.0006` n `25`; metal avg `0.0068` n `20`; unknown avg `-0.0367` n `791`
- 4h: commodity avg `-0.0409` n `12`; crypto_alt avg `-0.3721` n `230`; crypto_major avg `-0.2602` n `8`; equity avg `0.0109` n `114`; fx avg `0.0037` n `6`; index avg `0.0126` n `25`; metal avg `-0.0012` n `20`; unknown avg `0.0686` n `791`
- 24h: commodity avg `-0.1487` n `12`; crypto_alt avg `0.1131` n `230`; crypto_major avg `0.0416` n `8`; equity avg `0.2204` n `114`; fx avg `0.0405` n `6`; index avg `0.0129` n `25`; metal avg `-0.0314` n `20`; unknown avg `0.065` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2219`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1705`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
