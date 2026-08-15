# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T07:52:26.549964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `0.008` n `230`; crypto_major avg `-0.0056` n `8`; equity avg `-0.0036` n `114`; fx avg `0.0012` n `6`; index avg `-0.0068` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.0051` n `791`
- 1h: commodity avg `-0.1423` n `12`; crypto_alt avg `-0.1024` n `230`; crypto_major avg `-0.1064` n `8`; equity avg `0.0164` n `114`; fx avg `-0.0028` n `6`; index avg `0.006` n `25`; metal avg `-0.0061` n `20`; unknown avg `0.046` n `791`
- 4h: commodity avg `-0.1821` n `12`; crypto_alt avg `0.286` n `230`; crypto_major avg `-0.1458` n `8`; equity avg `-0.0239` n `114`; fx avg `-0.0114` n `6`; index avg `-0.0148` n `25`; metal avg `-0.0063` n `20`; unknown avg `-0.1112` n `759`
- 24h: commodity avg `-0.2817` n `12`; crypto_alt avg `1.0294` n `230`; crypto_major avg `0.0974` n `8`; equity avg `-0.1378` n `114`; fx avg `0.1298` n `6`; index avg `-0.074` n `25`; metal avg `0.2114` n `20`; unknown avg `-0.1315` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2157`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.19`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1768`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1744`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1566`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.155`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.147`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1434`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1419`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `669`, weak_sample_signal
