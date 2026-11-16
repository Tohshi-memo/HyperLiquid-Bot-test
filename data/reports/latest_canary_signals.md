# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T23:07:29.967042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.05` n `13`; crypto_alt avg `-0.0795` n `239`; crypto_major avg `-0.107` n `8`; equity avg `-0.1019` n `162`; fx avg `-0.0008` n `6`; index avg `-0.0127` n `27`; metal avg `0.017` n `20`; unknown avg `-0.0498` n `1260`
- 1h: commodity avg `0.0527` n `13`; crypto_alt avg `-0.3543` n `239`; crypto_major avg `-0.3315` n `8`; equity avg `-0.0768` n `162`; fx avg `-0.0001` n `6`; index avg `0.0124` n `27`; metal avg `0.0149` n `20`; unknown avg `-0.1539` n `1232`
- 4h: commodity avg `-0.0927` n `13`; crypto_alt avg `0.1152` n `239`; crypto_major avg `0.8104` n `8`; equity avg `-0.5379` n `162`; fx avg `-0.0039` n `6`; index avg `-0.0592` n `27`; metal avg `-0.0084` n `20`; unknown avg `215.2935` n `1186`
- 24h: commodity avg `-0.8723` n `13`; crypto_alt avg `-0.5417` n `239`; crypto_major avg `-0.1194` n `8`; equity avg `-4.1575` n `162`; fx avg `-0.1123` n `6`; index avg `-0.4795` n `27`; metal avg `-0.6201` n `20`; unknown avg `509.3307` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
