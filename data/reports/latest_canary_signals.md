# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T22:07:27.028455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0175` n `12`; crypto_alt avg `-0.1264` n `232`; crypto_major avg `-0.2097` n `8`; equity avg `-0.0935` n `133`; fx avg `0.0112` n `6`; index avg `-0.0236` n `26`; metal avg `0.0054` n `20`; unknown avg `-0.0662` n `790`
- 1h: commodity avg `0.0047` n `12`; crypto_alt avg `-0.0764` n `232`; crypto_major avg `-0.2166` n `8`; equity avg `0.1599` n `133`; fx avg `0.0011` n `6`; index avg `0.0183` n `26`; metal avg `-0.0123` n `20`; unknown avg `-0.2433` n `786`
- 4h: commodity avg `0.0118` n `12`; crypto_alt avg `0.0318` n `232`; crypto_major avg `-0.0197` n `8`; equity avg `0.3893` n `133`; fx avg `-0.0256` n `6`; index avg `-0.003` n `26`; metal avg `0.0376` n `20`; unknown avg `0.0579` n `772`
- 24h: commodity avg `0.1247` n `12`; crypto_alt avg `-0.2338` n `232`; crypto_major avg `-0.3526` n `8`; equity avg `0.9684` n `133`; fx avg `-0.4012` n `6`; index avg `0.1118` n `26`; metal avg `0.4698` n `20`; unknown avg `0.2975` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0441`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.043`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.041`, n `668`, weak_sample_signal
