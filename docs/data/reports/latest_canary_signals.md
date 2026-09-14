# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T16:37:34.712302+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0229` n `12`; crypto_alt avg `-0.1742` n `233`; crypto_major avg `-0.2668` n `8`; equity avg `-0.0833` n `136`; fx avg `0.0046` n `6`; index avg `-0.0066` n `27`; metal avg `0.0283` n `20`; unknown avg `0.1893` n `888`
- 1h: commodity avg `0.0281` n `12`; crypto_alt avg `0.2821` n `233`; crypto_major avg `0.4067` n `8`; equity avg `0.042` n `136`; fx avg `0.0176` n `6`; index avg `0.0353` n `27`; metal avg `0.0246` n `20`; unknown avg `0.1419` n `886`
- 4h: commodity avg `-0.3486` n `12`; crypto_alt avg `0.3158` n `233`; crypto_major avg `0.5887` n `8`; equity avg `1.1296` n `136`; fx avg `-0.013` n `6`; index avg `0.1424` n `27`; metal avg `0.1721` n `20`; unknown avg `0.8477` n `872`
- 24h: commodity avg `0.4198` n `12`; crypto_alt avg `-0.0499` n `233`; crypto_major avg `1.6145` n `8`; equity avg `-0.3835` n `136`; fx avg `0.0419` n `6`; index avg `-0.176` n `27`; metal avg `-0.3201` n `20`; unknown avg `0.8979` n `636`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
