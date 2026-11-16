# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T16:22:29.681732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0843` n `13`; crypto_alt avg `0.1248` n `239`; crypto_major avg `0.2076` n `8`; equity avg `0.144` n `162`; fx avg `-0.0082` n `6`; index avg `0.007` n `27`; metal avg `-0.0124` n `20`; unknown avg `3.9051` n `1265`
- 1h: commodity avg `0.0197` n `13`; crypto_alt avg `0.6886` n `239`; crypto_major avg `0.7584` n `8`; equity avg `0.7171` n `162`; fx avg `-0.0214` n `6`; index avg `0.1064` n `27`; metal avg `-0.0285` n `20`; unknown avg `12.6669` n `1239`
- 4h: commodity avg `-0.3568` n `13`; crypto_alt avg `0.8846` n `239`; crypto_major avg `0.8465` n `8`; equity avg `-0.039` n `162`; fx avg `-0.0047` n `6`; index avg `0.0913` n `27`; metal avg `-0.2564` n `20`; unknown avg `12.2114` n `1227`
- 24h: commodity avg `-0.7743` n `13`; crypto_alt avg `0.0132` n `239`; crypto_major avg `0.2995` n `8`; equity avg `-1.6288` n `162`; fx avg `-0.0425` n `6`; index avg `-0.1086` n `27`; metal avg `-0.1924` n `20`; unknown avg `255.338` n `1037`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
