# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T00:37:26.781246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `13`; crypto_alt avg `-0.1031` n `239`; crypto_major avg `0.0235` n `8`; equity avg `-0.1315` n `162`; fx avg `0.0015` n `6`; index avg `-0.0122` n `27`; metal avg `0.0232` n `20`; unknown avg `13.6856` n `1266`
- 1h: commodity avg `-0.0046` n `13`; crypto_alt avg `0.0249` n `239`; crypto_major avg `-0.2538` n `8`; equity avg `0.234` n `162`; fx avg `0.0028` n `6`; index avg `0.004` n `27`; metal avg `0.0404` n `20`; unknown avg `160.9827` n `1258`
- 4h: commodity avg `-0.079` n `13`; crypto_alt avg `-0.3086` n `239`; crypto_major avg `-0.1121` n `8`; equity avg `-0.1243` n `162`; fx avg `0.003` n `6`; index avg `-0.011` n `27`; metal avg `0.0432` n `20`; unknown avg `2.325` n `1188`
- 24h: commodity avg `-0.9645` n `13`; crypto_alt avg `-0.3869` n `239`; crypto_major avg `-0.201` n `8`; equity avg `-4.3956` n `162`; fx avg `-0.0806` n `6`; index avg `-0.4881` n `27`; metal avg `-0.5864` n `20`; unknown avg `510.8476` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
