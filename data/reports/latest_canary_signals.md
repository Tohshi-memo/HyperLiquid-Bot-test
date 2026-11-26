# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T07:07:27.599338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0434` n `13`; crypto_alt avg `0.1568` n `239`; crypto_major avg `0.1297` n `8`; equity avg `0.0587` n `168`; fx avg `0.0029` n `6`; index avg `0.0055` n `27`; metal avg `0.0351` n `20`; unknown avg `1.6309` n `1257`
- 1h: commodity avg `-0.1981` n `13`; crypto_alt avg `-0.3121` n `239`; crypto_major avg `-0.2792` n `8`; equity avg `-0.1307` n `168`; fx avg `0.0086` n `6`; index avg `-0.0273` n `27`; metal avg `-0.0788` n `20`; unknown avg `177.5972` n `1257`
- 4h: commodity avg `-0.2118` n `13`; crypto_alt avg `-0.4882` n `239`; crypto_major avg `-0.532` n `8`; equity avg `-0.5012` n `168`; fx avg `-0.0077` n `6`; index avg `-0.0597` n `27`; metal avg `-0.1731` n `20`; unknown avg `2.1796` n `1217`
- 24h: commodity avg `0.6117` n `13`; crypto_alt avg `2.4711` n `239`; crypto_major avg `2.0895` n `8`; equity avg `2.3724` n `168`; fx avg `0.0547` n `6`; index avg `0.1558` n `27`; metal avg `0.6062` n `20`; unknown avg `763.311` n `1027`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
