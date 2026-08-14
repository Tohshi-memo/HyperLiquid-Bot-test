# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T16:52:35.479649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0357` n `12`; crypto_alt avg `-0.0937` n `230`; crypto_major avg `-0.1` n `8`; equity avg `-0.0888` n `114`; fx avg `-0.0186` n `6`; index avg `-0.0133` n `25`; metal avg `0.0019` n `20`; unknown avg `-0.0177` n `791`
- 1h: commodity avg `0.0255` n `12`; crypto_alt avg `0.3865` n `230`; crypto_major avg `0.0376` n `8`; equity avg `0.1371` n `114`; fx avg `-0.0033` n `6`; index avg `0.0164` n `25`; metal avg `0.0027` n `20`; unknown avg `18.8326` n `791`
- 4h: commodity avg `0.156` n `12`; crypto_alt avg `0.772` n `230`; crypto_major avg `0.3058` n `8`; equity avg `-0.9053` n `114`; fx avg `0.1082` n `6`; index avg `-0.1729` n `25`; metal avg `0.1205` n `20`; unknown avg `0.0431` n `786`
- 24h: commodity avg `0.0509` n `12`; crypto_alt avg `0.7143` n `230`; crypto_major avg `-0.354` n `8`; equity avg `-0.4937` n `114`; fx avg `0.0847` n `6`; index avg `-0.1172` n `25`; metal avg `0.1569` n `20`; unknown avg `0.4346` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1864`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
