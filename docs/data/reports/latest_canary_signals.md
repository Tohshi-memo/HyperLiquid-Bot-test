# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T22:07:17.809432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1049` n `12`; crypto_alt avg `-0.3484` n `228`; crypto_major avg `-0.2194` n `8`; equity avg `0.0206` n `66`; fx avg `0.0016` n `6`; index avg `-0.0474` n `23`; metal avg `0.0269` n `18`; unknown avg `0.1141` n `383`
- 1h: commodity avg `0.1079` n `12`; crypto_alt avg `-0.2498` n `228`; crypto_major avg `-0.2809` n `8`; equity avg `0.0873` n `66`; fx avg `-0.0076` n `6`; index avg `0.0322` n `23`; metal avg `0.0967` n `18`; unknown avg `0.0112` n `383`
- 4h: commodity avg `0.4187` n `12`; crypto_alt avg `-0.5679` n `228`; crypto_major avg `-0.4339` n `8`; equity avg `-0.5999` n `66`; fx avg `0.01` n `6`; index avg `-0.3535` n `23`; metal avg `-0.3447` n `18`; unknown avg `-0.1835` n `383`
- 24h: commodity avg `1.1618` n `12`; crypto_alt avg `-1.1447` n `228`; crypto_major avg `-0.8459` n `8`; equity avg `-0.0767` n `66`; fx avg `0.0646` n `6`; index avg `-0.7444` n `23`; metal avg `-2.6883` n `18`; unknown avg `0.8825` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
