# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T08:22:28.438676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1494` n `12`; crypto_alt avg `-0.4415` n `234`; crypto_major avg `-0.4263` n `8`; equity avg `-0.3263` n `141`; fx avg `0.0422` n `6`; index avg `-0.0515` n `26`; metal avg `-0.1831` n `20`; unknown avg `0.8709` n `945`
- 1h: commodity avg `0.3975` n `12`; crypto_alt avg `-0.0154` n `234`; crypto_major avg `-0.1234` n `8`; equity avg `-0.3957` n `141`; fx avg `0.0105` n `6`; index avg `-0.0851` n `26`; metal avg `-0.1665` n `20`; unknown avg `1.6164` n `937`
- 4h: commodity avg `0.4894` n `12`; crypto_alt avg `0.7751` n `234`; crypto_major avg `0.5321` n `8`; equity avg `-0.507` n `141`; fx avg `0.0323` n `6`; index avg `-0.1096` n `26`; metal avg `-0.0987` n `20`; unknown avg `3.1269` n `921`
- 24h: commodity avg `0.8467` n `12`; crypto_alt avg `-3.9997` n `234`; crypto_major avg `-3.5628` n `8`; equity avg `-2.5144` n `140`; fx avg `0.0122` n `6`; index avg `-0.4824` n `26`; metal avg `-0.5241` n `20`; unknown avg `588.2301` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
