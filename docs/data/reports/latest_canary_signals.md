# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T00:24:46.627011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0206` n `12`; crypto_alt avg `0.0394` n `230`; crypto_major avg `-0.0149` n `8`; equity avg `0.0066` n `114`; fx avg `-0.0025` n `6`; index avg `0.0004` n `25`; metal avg `0.005` n `20`; unknown avg `-0.0187` n `791`
- 1h: commodity avg `0.0744` n `12`; crypto_alt avg `0.1882` n `230`; crypto_major avg `0.18` n `8`; equity avg `-0.0754` n `114`; fx avg `-0.0262` n `6`; index avg `-0.0057` n `25`; metal avg `0.0395` n `20`; unknown avg `0.0777` n `791`
- 4h: commodity avg `0.1238` n `12`; crypto_alt avg `0.3937` n `230`; crypto_major avg `0.2992` n `8`; equity avg `0.0048` n `114`; fx avg `-0.034` n `6`; index avg `-0.0073` n `25`; metal avg `0.0884` n `20`; unknown avg `2.6217` n `791`
- 24h: commodity avg `0.273` n `12`; crypto_alt avg `0.0818` n `230`; crypto_major avg `-0.7433` n `8`; equity avg `-0.474` n `114`; fx avg `0.0606` n `6`; index avg `-0.1001` n `25`; metal avg `0.3144` n `20`; unknown avg `-0.2909` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1953`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1681`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
