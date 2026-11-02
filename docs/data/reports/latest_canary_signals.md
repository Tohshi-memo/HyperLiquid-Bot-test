# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T13:37:28.912441+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2499` n `13`; crypto_alt avg `0.4556` n `239`; crypto_major avg `0.488` n `8`; equity avg `0.2874` n `156`; fx avg `-0.008` n `6`; index avg `0.0675` n `27`; metal avg `0.1566` n `20`; unknown avg `0.9149` n `1265`
- 1h: commodity avg `-0.296` n `13`; crypto_alt avg `0.1933` n `238`; crypto_major avg `0.1755` n `8`; equity avg `-0.1287` n `156`; fx avg `-0.0016` n `6`; index avg `0.0491` n `27`; metal avg `0.15` n `20`; unknown avg `2.8565` n `1259`
- 4h: commodity avg `-0.212` n `13`; crypto_alt avg `0.1904` n `238`; crypto_major avg `0.0146` n `8`; equity avg `-0.541` n `156`; fx avg `-0.0038` n `6`; index avg `0.0082` n `27`; metal avg `0.048` n `20`; unknown avg `3.8171` n `1254`
- 24h: commodity avg `-0.7327` n `13`; crypto_alt avg `-2.1408` n `238`; crypto_major avg `-0.3964` n `8`; equity avg `0.3479` n `156`; fx avg `0.2882` n `6`; index avg `0.3037` n `27`; metal avg `0.1029` n `20`; unknown avg `7.0721` n `1079`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1916`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1879`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1783`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
