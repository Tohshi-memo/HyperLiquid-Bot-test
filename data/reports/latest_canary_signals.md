# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T07:37:24.242204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `13`; crypto_alt avg `-0.0332` n `239`; crypto_major avg `0.0532` n `8`; equity avg `0.0892` n `161`; fx avg `0.0055` n `6`; index avg `0.0067` n `27`; metal avg `-0.0067` n `20`; unknown avg `1.4787` n `1262`
- 1h: commodity avg `0.1144` n `13`; crypto_alt avg `0.0665` n `239`; crypto_major avg `0.0617` n `8`; equity avg `0.0992` n `161`; fx avg `0.043` n `6`; index avg `-0.0051` n `27`; metal avg `-0.0751` n `20`; unknown avg `1.4462` n `1256`
- 4h: commodity avg `0.2371` n `13`; crypto_alt avg `-0.3565` n `239`; crypto_major avg `-0.2999` n `8`; equity avg `-0.5611` n `161`; fx avg `0.0377` n `6`; index avg `-0.0797` n `27`; metal avg `-0.1335` n `20`; unknown avg `0.1248` n `1206`
- 24h: commodity avg `0.346` n `13`; crypto_alt avg `-1.2143` n `239`; crypto_major avg `-0.5487` n `8`; equity avg `-0.2975` n `161`; fx avg `-0.1297` n `6`; index avg `-0.0668` n `27`; metal avg `-0.7114` n `20`; unknown avg `0.5414` n `1125`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
