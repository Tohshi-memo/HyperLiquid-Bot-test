# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T11:37:30.574215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0215` n `12`; crypto_alt avg `-0.1037` n `230`; crypto_major avg `-0.1182` n `8`; equity avg `0.1569` n `113`; fx avg `-0.0017` n `6`; index avg `0.0159` n `25`; metal avg `0.0009` n `20`; unknown avg `0.04` n `787`
- 1h: commodity avg `0.0135` n `12`; crypto_alt avg `-0.1444` n `230`; crypto_major avg `-0.2491` n `8`; equity avg `0.2224` n `113`; fx avg `-0.02` n `6`; index avg `0.0246` n `25`; metal avg `-0.0013` n `20`; unknown avg `0.4879` n `787`
- 4h: commodity avg `-0.1795` n `12`; crypto_alt avg `-0.2506` n `230`; crypto_major avg `-0.7598` n `8`; equity avg `0.0217` n `113`; fx avg `0.0023` n `6`; index avg `0.009` n `25`; metal avg `0.0817` n `20`; unknown avg `0.5004` n `787`
- 24h: commodity avg `-0.3708` n `12`; crypto_alt avg `-0.756` n `230`; crypto_major avg `-0.8649` n `8`; equity avg `1.4375` n `113`; fx avg `0.0223` n `6`; index avg `0.1683` n `25`; metal avg `-0.5791` n `20`; unknown avg `0.6791` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2251`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
