# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T05:22:26.874457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `-0.0645` n `230`; crypto_major avg `-0.069` n `8`; equity avg `0.0198` n `114`; fx avg `0.0054` n `6`; index avg `0.0036` n `25`; metal avg `-0.0026` n `20`; unknown avg `0.0324` n `791`
- 1h: commodity avg `-0.0476` n `12`; crypto_alt avg `-0.0037` n `230`; crypto_major avg `-0.1078` n `8`; equity avg `-0.0018` n `114`; fx avg `0.0018` n `6`; index avg `0.0075` n `25`; metal avg `-0.0027` n `20`; unknown avg `0.5943` n `791`
- 4h: commodity avg `-0.0092` n `12`; crypto_alt avg `-0.2048` n `230`; crypto_major avg `-0.0565` n `8`; equity avg `0.1632` n `114`; fx avg `0.0028` n `6`; index avg `0.0113` n `25`; metal avg `0.0069` n `20`; unknown avg `-0.015` n `791`
- 24h: commodity avg `-0.0895` n `12`; crypto_alt avg `-0.4029` n `230`; crypto_major avg `-0.1391` n `8`; equity avg `0.2771` n `114`; fx avg `-0.0151` n `6`; index avg `0.033` n `25`; metal avg `0.0111` n `20`; unknown avg `0.0337` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2219`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
