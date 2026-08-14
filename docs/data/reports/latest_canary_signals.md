# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T12:37:24.208619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1077` n `12`; crypto_alt avg `0.017` n `230`; crypto_major avg `0.0481` n `8`; equity avg `0.2292` n `114`; fx avg `-0.0247` n `6`; index avg `0.0344` n `25`; metal avg `-0.0151` n `20`; unknown avg `0.0429` n `786`
- 1h: commodity avg `0.0138` n `12`; crypto_alt avg `-0.2091` n `230`; crypto_major avg `-0.1248` n `8`; equity avg `0.0186` n `114`; fx avg `-0.0375` n `6`; index avg `-0.0032` n `25`; metal avg `0.0456` n `20`; unknown avg `0.0138` n `786`
- 4h: commodity avg `-0.1648` n `12`; crypto_alt avg `-0.4076` n `230`; crypto_major avg `-0.3449` n `8`; equity avg `0.2685` n `114`; fx avg `0.0126` n `6`; index avg `0.0453` n `25`; metal avg `0.1374` n `20`; unknown avg `3.423` n `786`
- 24h: commodity avg `-0.1218` n `12`; crypto_alt avg `-0.9474` n `230`; crypto_major avg `-0.8767` n `8`; equity avg `1.9153` n `114`; fx avg `-0.058` n `6`; index avg `0.352` n `25`; metal avg `-0.061` n `20`; unknown avg `0.9712` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2183`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1873`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1694`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
