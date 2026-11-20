# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T00:22:29.680695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.8561` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0043` n `13`; crypto_alt avg `0.1215` n `239`; crypto_major avg `0.2348` n `8`; equity avg `0.1178` n `165`; fx avg `0.004` n `6`; index avg `0.036` n `27`; metal avg `0.0722` n `20`; unknown avg `0.0973` n `1260`
- 1h: commodity avg `-0.0213` n `13`; crypto_alt avg `0.1452` n `239`; crypto_major avg `0.286` n `8`; equity avg `-0.0386` n `165`; fx avg `0.0227` n `6`; index avg `0.0323` n `27`; metal avg `-0.0052` n `20`; unknown avg `0.0016` n `1252`
- 4h: commodity avg `0.0183` n `13`; crypto_alt avg `0.1526` n `239`; crypto_major avg `0.0975` n `8`; equity avg `-1.7586` n `165`; fx avg `0.0193` n `6`; index avg `-0.0277` n `27`; metal avg `-0.3821` n `20`; unknown avg `14.1727` n `1230`
- 24h: commodity avg `0.0554` n `13`; crypto_alt avg `-0.5114` n `239`; crypto_major avg `0.0453` n `8`; equity avg `-4.1757` n `165`; fx avg `0.0495` n `6`; index avg `-0.2366` n `27`; metal avg `-1.0497` n `20`; unknown avg `20.5944` n `1172`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
