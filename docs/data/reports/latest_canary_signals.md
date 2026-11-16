# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T19:52:45.196137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `13`; crypto_alt avg `0.1603` n `239`; crypto_major avg `0.2714` n `8`; equity avg `0.0295` n `162`; fx avg `0.0082` n `6`; index avg `-0.0053` n `27`; metal avg `-0.0002` n `20`; unknown avg `161.151` n `1266`
- 1h: commodity avg `0.0206` n `13`; crypto_alt avg `-0.1944` n `239`; crypto_major avg `-0.0829` n `8`; equity avg `-0.023` n `162`; fx avg `0.0214` n `6`; index avg `-0.0328` n `27`; metal avg `0.047` n `20`; unknown avg `3.0638` n `1264`
- 4h: commodity avg `-0.4174` n `13`; crypto_alt avg `0.4349` n `239`; crypto_major avg `0.5679` n `8`; equity avg `-0.4563` n `162`; fx avg `-0.0075` n `6`; index avg `-0.1066` n `27`; metal avg `-0.0359` n `20`; unknown avg `4.0651` n `1249`
- 24h: commodity avg `-1.1302` n `13`; crypto_alt avg `-0.0134` n `239`; crypto_major avg `0.0787` n `8`; equity avg `-2.8114` n `162`; fx avg `-0.098` n `6`; index avg `-0.2861` n `27`; metal avg `-0.259` n `20`; unknown avg `252.8116` n `1037`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1359`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1258`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1191`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1095`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1032`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1005`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0951`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0879`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `669`, weak_sample_signal
