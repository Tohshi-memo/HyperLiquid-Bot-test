# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T16:52:28.240998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.063` n `232`; crypto_major avg `0.0318` n `8`; equity avg `0.0039` n `134`; fx avg `0.013` n `6`; index avg `-0.0017` n `26`; metal avg `-0.0001` n `20`; unknown avg `144.686` n `793`
- 1h: commodity avg `0.0067` n `12`; crypto_alt avg `0.2971` n `232`; crypto_major avg `0.1305` n `8`; equity avg `-0.0019` n `134`; fx avg `0.0091` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0091` n `20`; unknown avg `-0.0894` n `785`
- 4h: commodity avg `0.0377` n `12`; crypto_alt avg `-0.2532` n `232`; crypto_major avg `-0.6494` n `8`; equity avg `-0.2863` n `134`; fx avg `0.0024` n `6`; index avg `-0.0321` n `26`; metal avg `-0.0293` n `20`; unknown avg `0.5673` n `720`
- 24h: commodity avg `0.1111` n `12`; crypto_alt avg `1.6439` n `232`; crypto_major avg `0.4132` n `8`; equity avg `0.2202` n `134`; fx avg `-0.0283` n `6`; index avg `0.0138` n `26`; metal avg `-0.0433` n `20`; unknown avg `1.4343` n `664`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
