# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T02:37:26.705685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `0.0682` n `233`; crypto_major avg `0.2231` n `8`; equity avg `0.0168` n `136`; fx avg `0.0037` n `6`; index avg `0.0016` n `27`; metal avg `0.0292` n `20`; unknown avg `0.8923` n `894`
- 1h: commodity avg `-0.0847` n `12`; crypto_alt avg `1.2714` n `233`; crypto_major avg `1.1594` n `8`; equity avg `0.5256` n `136`; fx avg `0.0143` n `6`; index avg `0.0886` n `27`; metal avg `0.0858` n `20`; unknown avg `4.532` n `892`
- 4h: commodity avg `-0.0139` n `12`; crypto_alt avg `1.3848` n `233`; crypto_major avg `1.0504` n `8`; equity avg `-0.0136` n `136`; fx avg `0.0013` n `6`; index avg `-0.0201` n `27`; metal avg `0.116` n `20`; unknown avg `14.6861` n `768`
- 24h: commodity avg `0.6443` n `12`; crypto_alt avg `-0.5305` n `233`; crypto_major avg `-0.5358` n `8`; equity avg `-1.3566` n `136`; fx avg `0.0654` n `6`; index avg `-0.295` n `26`; metal avg `-0.0234` n `20`; unknown avg `1.648` n `682`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
