# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T22:22:28.612524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0617` n `13`; crypto_alt avg `-0.0846` n `239`; crypto_major avg `-0.1308` n `8`; equity avg `0.061` n `162`; fx avg `0.0027` n `6`; index avg `0.0124` n `27`; metal avg `0.0053` n `20`; unknown avg `0.0425` n `1264`
- 1h: commodity avg `-0.0257` n `13`; crypto_alt avg `0.3831` n `239`; crypto_major avg `0.6173` n `8`; equity avg `0.031` n `162`; fx avg `0.0197` n `6`; index avg `-0.0073` n `27`; metal avg `0.0388` n `20`; unknown avg `0.1193` n `1256`
- 4h: commodity avg `-0.2405` n `13`; crypto_alt avg `0.4109` n `239`; crypto_major avg `1.0253` n `8`; equity avg `-0.2052` n `162`; fx avg `0.0054` n `6`; index avg `-0.0706` n `27`; metal avg `0.0487` n `20`; unknown avg `2.7115` n `1218`
- 24h: commodity avg `-1.1472` n `13`; crypto_alt avg `0.0035` n `239`; crypto_major avg `0.422` n `8`; equity avg `-3.4213` n `162`; fx avg `-0.1147` n `6`; index avg `-0.3415` n `27`; metal avg `-0.3408` n `20`; unknown avg `496.6681` n `1027`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
