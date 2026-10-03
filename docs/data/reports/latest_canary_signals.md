# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T06:22:27.323144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.43` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0003` n `13`; crypto_alt avg `-0.0815` n `235`; crypto_major avg `-0.047` n `8`; equity avg `-0.023` n `143`; fx avg `0.0031` n `6`; index avg `-0.0056` n `26`; metal avg `0.0002` n `20`; unknown avg `0.0186` n `984`
- 1h: commodity avg `-0.0057` n `13`; crypto_alt avg `-0.197` n `235`; crypto_major avg `-0.0617` n `8`; equity avg `-0.0321` n `143`; fx avg `0.0075` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0019` n `20`; unknown avg `2.5738` n `960`
- 4h: commodity avg `-0.0793` n `13`; crypto_alt avg `-0.0778` n `235`; crypto_major avg `-0.2223` n `8`; equity avg `-0.1206` n `143`; fx avg `-0.0048` n `6`; index avg `-0.0171` n `26`; metal avg `-0.002` n `20`; unknown avg `-0.1806` n `954`
- 24h: commodity avg `0.0928` n `13`; crypto_alt avg `-1.5441` n `235`; crypto_major avg `-1.9276` n `8`; equity avg `0.461` n `142`; fx avg `-0.0261` n `6`; index avg `0.2427` n `26`; metal avg `-0.3699` n `20`; unknown avg `-0.8674` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1762`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
