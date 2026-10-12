# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T09:43:22.704628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1062` n `13`; crypto_alt avg `-0.2369` n `235`; crypto_major avg `-0.124` n `8`; equity avg `-0.0537` n `151`; fx avg `0.0185` n `6`; index avg `-0.0261` n `26`; metal avg `-0.0251` n `20`; unknown avg `-0.1117` n `1107`
- 1h: commodity avg `0.2144` n `13`; crypto_alt avg `-0.4048` n `235`; crypto_major avg `-0.4078` n `8`; equity avg `-0.1869` n `151`; fx avg `0.0175` n `6`; index avg `-0.059` n `26`; metal avg `-0.0288` n `20`; unknown avg `0.0624` n `1041`
- 4h: commodity avg `0.3986` n `13`; crypto_alt avg `-0.803` n `235`; crypto_major avg `-0.4862` n `8`; equity avg `-0.7352` n `151`; fx avg `-0.0495` n `6`; index avg `-0.1118` n `26`; metal avg `-0.0731` n `20`; unknown avg `0.7246` n `981`
- 24h: commodity avg `-0.02` n `13`; crypto_alt avg `1.7728` n `235`; crypto_major avg `1.1949` n `8`; equity avg `-1.1084` n `151`; fx avg `-0.0931` n `6`; index avg `-0.1373` n `26`; metal avg `-0.0149` n `20`; unknown avg `0.0776` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
