# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T15:52:31.387871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.0046` n `233`; crypto_major avg `-0.0041` n `8`; equity avg `0.0176` n `136`; fx avg `-0.0048` n `6`; index avg `0.0016` n `26`; metal avg `0.0063` n `20`; unknown avg `-0.1302` n `838`
- 1h: commodity avg `-0.0096` n `12`; crypto_alt avg `0.1353` n `233`; crypto_major avg `-0.1085` n `8`; equity avg `0.007` n `136`; fx avg `-0.0025` n `6`; index avg `0.0076` n `26`; metal avg `0.0047` n `20`; unknown avg `0.2819` n `836`
- 4h: commodity avg `-0.0422` n `12`; crypto_alt avg `0.2202` n `233`; crypto_major avg `-0.0873` n `8`; equity avg `-0.0142` n `136`; fx avg `0.0016` n `6`; index avg `0.0161` n `26`; metal avg `0.0073` n `20`; unknown avg `2.0526` n `824`
- 24h: commodity avg `-0.1632` n `12`; crypto_alt avg `-0.1074` n `233`; crypto_major avg `-1.0552` n `8`; equity avg `-0.3971` n `136`; fx avg `-0.0196` n `6`; index avg `-0.0164` n `26`; metal avg `-0.0824` n `20`; unknown avg `11.3335` n `694`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
