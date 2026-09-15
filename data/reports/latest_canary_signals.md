# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T10:37:32.040950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0343` n `12`; crypto_alt avg `0.0161` n `233`; crypto_major avg `0.0645` n `8`; equity avg `0.1046` n `136`; fx avg `0.0011` n `6`; index avg `0.0187` n `27`; metal avg `0.0152` n `20`; unknown avg `1.3309` n `908`
- 1h: commodity avg `-0.1193` n `12`; crypto_alt avg `-0.1701` n `233`; crypto_major avg `0.0955` n `8`; equity avg `0.4683` n `136`; fx avg `-0.0309` n `6`; index avg `0.0781` n `27`; metal avg `0.0985` n `20`; unknown avg `1.7697` n `904`
- 4h: commodity avg `-0.0468` n `12`; crypto_alt avg `-0.5165` n `233`; crypto_major avg `-0.254` n `8`; equity avg `0.2518` n `136`; fx avg `0.039` n `6`; index avg `0.0282` n `27`; metal avg `-0.036` n `20`; unknown avg `1.2438` n `896`
- 24h: commodity avg `0.0025` n `12`; crypto_alt avg `-1.5086` n `233`; crypto_major avg `-0.8647` n `8`; equity avg `0.2339` n `136`; fx avg `0.2015` n `6`; index avg `0.0207` n `27`; metal avg `-0.0215` n `20`; unknown avg `0.2328` n `818`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
