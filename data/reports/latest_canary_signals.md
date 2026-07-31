# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T06:52:30.506665+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0648` n `12`; crypto_alt avg `0.0084` n `230`; crypto_major avg `-0.0698` n `8`; equity avg `-0.0799` n `102`; fx avg `-0.0063` n `6`; index avg `-0.0128` n `25`; metal avg `-0.0177` n `20`; unknown avg `-0.0068` n `779`
- 1h: commodity avg `0.1535` n `12`; crypto_alt avg `0.142` n `230`; crypto_major avg `0.1291` n `8`; equity avg `-0.6857` n `102`; fx avg `-0.1446` n `6`; index avg `-0.115` n `25`; metal avg `0.0398` n `20`; unknown avg `0.0006` n `747`
- 4h: commodity avg `0.0197` n `12`; crypto_alt avg `0.2047` n `230`; crypto_major avg `0.2265` n `8`; equity avg `0.1588` n `102`; fx avg `-0.1088` n `6`; index avg `0.0531` n `25`; metal avg `0.0328` n `20`; unknown avg `0.0186` n `747`
- 24h: commodity avg `-0.512` n `12`; crypto_alt avg `0.2498` n `230`; crypto_major avg `1.1476` n `8`; equity avg `8.4185` n `102`; fx avg `-0.1875` n `6`; index avg `1.2447` n `25`; metal avg `0.6299` n `20`; unknown avg `0.0859` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
