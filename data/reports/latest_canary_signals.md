# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T03:22:28.565270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0233` n `12`; crypto_alt avg `-0.352` n `233`; crypto_major avg `-0.1363` n `8`; equity avg `-0.0948` n `136`; fx avg `-0.0032` n `6`; index avg `-0.0107` n `27`; metal avg `0.008` n `20`; unknown avg `0.3022` n `904`
- 1h: commodity avg `0.0138` n `12`; crypto_alt avg `-0.5346` n `233`; crypto_major avg `-0.4344` n `8`; equity avg `-0.1461` n `136`; fx avg `-0.0253` n `6`; index avg `-0.0082` n `27`; metal avg `0.0704` n `20`; unknown avg `0.3074` n `902`
- 4h: commodity avg `0.0517` n `12`; crypto_alt avg `-0.7042` n `233`; crypto_major avg `-0.669` n `8`; equity avg `0.1134` n `136`; fx avg `0.1062` n `6`; index avg `0.0793` n `27`; metal avg `0.1582` n `20`; unknown avg `0.5752` n `896`
- 24h: commodity avg `-0.1036` n `12`; crypto_alt avg `-1.1165` n `233`; crypto_major avg `0.0577` n `8`; equity avg `-0.1521` n `136`; fx avg `0.0982` n `6`; index avg `-0.0189` n `27`; metal avg `-0.2473` n `20`; unknown avg `5.4078` n `790`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
