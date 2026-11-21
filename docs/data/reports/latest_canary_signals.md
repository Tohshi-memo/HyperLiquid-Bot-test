# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T02:52:25.564135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `13`; crypto_alt avg `-0.0812` n `239`; crypto_major avg `-0.1104` n `8`; equity avg `0.085` n `166`; fx avg `-0.0008` n `6`; index avg `0.0114` n `27`; metal avg `0.0101` n `20`; unknown avg `158.4761` n `1262`
- 1h: commodity avg `0.0333` n `13`; crypto_alt avg `-0.2362` n `239`; crypto_major avg `-0.5594` n `8`; equity avg `-0.1588` n `166`; fx avg `-0.0104` n `6`; index avg `-0.0138` n `27`; metal avg `-0.0099` n `20`; unknown avg `1.7611` n `1258`
- 4h: commodity avg `-0.0032` n `13`; crypto_alt avg `-0.7165` n `239`; crypto_major avg `-0.7786` n `8`; equity avg `-0.0554` n `166`; fx avg `0.0018` n `6`; index avg `0.0136` n `27`; metal avg `0.0117` n `20`; unknown avg `5.804` n `1238`
- 24h: commodity avg `0.2998` n `13`; crypto_alt avg `-4.0796` n `239`; crypto_major avg `-5.3831` n `8`; equity avg `-4.8117` n `166`; fx avg `-0.0343` n `6`; index avg `-0.528` n `27`; metal avg `-0.2028` n `20`; unknown avg `12.6073` n `1119`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
