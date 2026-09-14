# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T02:52:32.416564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0433` n `12`; crypto_alt avg `0.1585` n `233`; crypto_major avg `0.2557` n `8`; equity avg `0.0299` n `136`; fx avg `0.0071` n `6`; index avg `0.0088` n `27`; metal avg `-0.0783` n `20`; unknown avg `0.5296` n `894`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `1.1306` n `233`; crypto_major avg `1.1963` n `8`; equity avg `0.3507` n `136`; fx avg `0.0216` n `6`; index avg `0.0657` n `27`; metal avg `-0.0269` n `20`; unknown avg `5.0712` n `892`
- 4h: commodity avg `0.0532` n `12`; crypto_alt avg `1.6593` n `233`; crypto_major avg `1.4148` n `8`; equity avg `0.0866` n `136`; fx avg `0.0133` n `6`; index avg `-0.0079` n `27`; metal avg `0.0373` n `20`; unknown avg `16.8941` n `768`
- 24h: commodity avg `0.6812` n `12`; crypto_alt avg `-0.4771` n `233`; crypto_major avg `-0.3863` n `8`; equity avg `-1.3047` n `136`; fx avg `0.075` n `6`; index avg `-0.2738` n `26`; metal avg `-0.1029` n `20`; unknown avg `1.8081` n `682`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
