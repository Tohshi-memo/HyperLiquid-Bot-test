# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T23:22:28.399283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `13`; crypto_alt avg `0.1217` n `239`; crypto_major avg `-0.0007` n `8`; equity avg `0.0018` n `165`; fx avg `0.0207` n `6`; index avg `0.0141` n `27`; metal avg `-0.041` n `20`; unknown avg `23.7559` n `1260`
- 1h: commodity avg `0.0013` n `13`; crypto_alt avg `0.41` n `239`; crypto_major avg `0.3281` n `8`; equity avg `-0.2809` n `165`; fx avg `0.0097` n `6`; index avg `-0.009` n `27`; metal avg `-0.0483` n `20`; unknown avg `17.8299` n `1256`
- 4h: commodity avg `0.053` n `13`; crypto_alt avg `-0.4672` n `239`; crypto_major avg `-1.0131` n `8`; equity avg `-2.4488` n `165`; fx avg `-0.0137` n `6`; index avg `-0.1518` n `27`; metal avg `-0.4648` n `20`; unknown avg `3.7876` n `1230`
- 24h: commodity avg `0.0542` n `13`; crypto_alt avg `-0.6602` n `239`; crypto_major avg `-0.5297` n `8`; equity avg `-4.0689` n `165`; fx avg `-0.0284` n `6`; index avg `-0.2711` n `27`; metal avg `-1.0165` n `20`; unknown avg `8.7494` n `1172`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
