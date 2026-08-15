# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T07:22:27.911446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2083` n `12`; crypto_alt avg `-0.0359` n `230`; crypto_major avg `-0.1169` n `8`; equity avg `0.0252` n `114`; fx avg `-0.0055` n `6`; index avg `0.0164` n `25`; metal avg `-0.0022` n `20`; unknown avg `0.0458` n `791`
- 1h: commodity avg `-0.2793` n `12`; crypto_alt avg `-0.0379` n `230`; crypto_major avg `-0.03` n `8`; equity avg `0.0678` n `114`; fx avg `-0.0061` n `6`; index avg `0.0247` n `25`; metal avg `0.0177` n `20`; unknown avg `-0.002` n `791`
- 4h: commodity avg `-0.2127` n `12`; crypto_alt avg `0.1392` n `230`; crypto_major avg `-0.2693` n `8`; equity avg `-0.0062` n `114`; fx avg `-0.0438` n `6`; index avg `-0.0115` n `25`; metal avg `-0.004` n `20`; unknown avg `-0.1202` n `759`
- 24h: commodity avg `-0.3178` n `12`; crypto_alt avg `0.9757` n `230`; crypto_major avg `-0.0078` n `8`; equity avg `-0.0567` n `114`; fx avg `0.0962` n `6`; index avg `-0.0534` n `25`; metal avg `0.3396` n `20`; unknown avg `-0.1438` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2157`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1906`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1773`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1755`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1578`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1566`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1473`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1419`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1399`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `669`, weak_sample_signal
