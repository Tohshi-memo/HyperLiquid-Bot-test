# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T04:37:31.721968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `13`; crypto_alt avg `0.2425` n `235`; crypto_major avg `0.1493` n `8`; equity avg `0.0096` n `150`; fx avg `0.0007` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.1605` n `1117`
- 1h: commodity avg `0.0024` n `13`; crypto_alt avg `-0.0771` n `235`; crypto_major avg `-0.0701` n `8`; equity avg `0.0008` n `150`; fx avg `0.0` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0048` n `20`; unknown avg `-0.0504` n `1109`
- 4h: commodity avg `0.0998` n `13`; crypto_alt avg `-0.4716` n `235`; crypto_major avg `-0.1578` n `8`; equity avg `-0.0764` n `150`; fx avg `0.0027` n `6`; index avg `-0.0166` n `26`; metal avg `-0.0016` n `20`; unknown avg `-0.3664` n `1109`
- 24h: commodity avg `0.1908` n `13`; crypto_alt avg `0.4047` n `235`; crypto_major avg `0.0828` n `8`; equity avg `-0.0333` n `150`; fx avg `-0.0119` n `6`; index avg `-0.0359` n `26`; metal avg `-0.0118` n `20`; unknown avg `0.2326` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
