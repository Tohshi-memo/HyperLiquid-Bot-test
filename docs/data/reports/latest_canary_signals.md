# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T13:39:19.429202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0886` n `12`; crypto_alt avg `0.1408` n `230`; crypto_major avg `0.153` n `8`; equity avg `-0.0563` n `92`; fx avg `-0.0134` n `6`; index avg `-0.0164` n `25`; metal avg `-0.055` n `20`; unknown avg `-0.0222` n `766`
- 1h: commodity avg `-0.2042` n `12`; crypto_alt avg `0.0954` n `230`; crypto_major avg `-0.0376` n `8`; equity avg `0.0572` n `92`; fx avg `-0.0326` n `6`; index avg `0.056` n `25`; metal avg `0.0611` n `20`; unknown avg `-0.1001` n `766`
- 4h: commodity avg `0.1803` n `12`; crypto_alt avg `-0.346` n `230`; crypto_major avg `-0.7935` n `8`; equity avg `-0.3552` n `92`; fx avg `-0.0352` n `6`; index avg `-0.0539` n `25`; metal avg `-0.0564` n `20`; unknown avg `-0.0272` n `766`
- 24h: commodity avg `-0.1408` n `12`; crypto_alt avg `-1.5222` n `230`; crypto_major avg `-2.1957` n `8`; equity avg `-2.2849` n `92`; fx avg `-0.0728` n `6`; index avg `-0.469` n `25`; metal avg `-0.2141` n `20`; unknown avg `-0.2321` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
