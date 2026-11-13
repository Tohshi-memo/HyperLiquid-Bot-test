# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T16:37:37.470929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.7866` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1046` n `13`; crypto_alt avg `0.3785` n `239`; crypto_major avg `0.2908` n `8`; equity avg `0.4103` n `162`; fx avg `-0.0073` n `6`; index avg `0.0437` n `27`; metal avg `0.0286` n `20`; unknown avg `5.818` n `1262`
- 1h: commodity avg `-0.1142` n `13`; crypto_alt avg `0.7758` n `239`; crypto_major avg `0.4772` n `8`; equity avg `0.536` n `162`; fx avg `-0.0364` n `6`; index avg `0.0258` n `27`; metal avg `-0.0341` n `20`; unknown avg `-0.4887` n `1254`
- 4h: commodity avg `-0.3133` n `13`; crypto_alt avg `-0.2284` n `239`; crypto_major avg `-1.0015` n `8`; equity avg `-2.7881` n `162`; fx avg `-0.0557` n `6`; index avg `-0.2811` n `27`; metal avg `-0.2294` n `20`; unknown avg `4.9051` n `1248`
- 24h: commodity avg `0.2433` n `13`; crypto_alt avg `0.4086` n `239`; crypto_major avg `-1.6395` n `8`; equity avg `-3.7111` n `162`; fx avg `-0.0383` n `6`; index avg `-0.3356` n `27`; metal avg `-0.1308` n `20`; unknown avg `2.2808` n `1075`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
