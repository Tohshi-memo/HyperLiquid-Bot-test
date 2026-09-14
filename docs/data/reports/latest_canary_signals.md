# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T17:37:26.834964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0847` n `12`; crypto_alt avg `-0.0256` n `233`; crypto_major avg `-0.0284` n `8`; equity avg `0.0386` n `136`; fx avg `0.0002` n `6`; index avg `0.0113` n `27`; metal avg `-0.008` n `20`; unknown avg `0.2146` n `908`
- 1h: commodity avg `-0.1571` n `12`; crypto_alt avg `0.4895` n `233`; crypto_major avg `0.3105` n `8`; equity avg `0.329` n `136`; fx avg `0.0225` n `6`; index avg `0.0368` n `27`; metal avg `0.0101` n `20`; unknown avg `0.8489` n `884`
- 4h: commodity avg `-0.2286` n `12`; crypto_alt avg `1.0163` n `233`; crypto_major avg `0.8846` n `8`; equity avg `1.3185` n `136`; fx avg `-0.0235` n `6`; index avg `0.1671` n `27`; metal avg `0.1907` n `20`; unknown avg `0.4572` n `864`
- 24h: commodity avg `0.2394` n `12`; crypto_alt avg `0.0424` n `233`; crypto_major avg `1.6741` n `8`; equity avg `-0.1493` n `136`; fx avg `0.063` n `6`; index avg `-0.1196` n `27`; metal avg `-0.3262` n `20`; unknown avg `0.9427` n `688`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
