# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T18:07:28.018583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0944` n `13`; crypto_alt avg `-0.2917` n `239`; crypto_major avg `-0.2024` n `8`; equity avg `-0.1669` n `162`; fx avg `0.0006` n `6`; index avg `-0.0173` n `27`; metal avg `-0.0522` n `20`; unknown avg `0.0141` n `1256`
- 1h: commodity avg `0.13` n `13`; crypto_alt avg `0.094` n `239`; crypto_major avg `0.161` n `8`; equity avg `-0.16` n `162`; fx avg `-0.0144` n `6`; index avg `-0.0082` n `27`; metal avg `-0.037` n `20`; unknown avg `0.9623` n `1258`
- 4h: commodity avg `-0.2436` n `13`; crypto_alt avg `-1.2067` n `239`; crypto_major avg `-1.1601` n `8`; equity avg `-2.6108` n `162`; fx avg `-0.0541` n `6`; index avg `-0.2405` n `27`; metal avg `-0.1917` n `20`; unknown avg `32.0164` n `1246`
- 24h: commodity avg `-0.074` n `13`; crypto_alt avg `-0.0253` n `239`; crypto_major avg `-1.7316` n `8`; equity avg `-3.2148` n `162`; fx avg `-0.024` n `6`; index avg `-0.2819` n `27`; metal avg `-0.2501` n `20`; unknown avg `2.3513` n `1089`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
