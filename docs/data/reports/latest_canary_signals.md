# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T21:07:21.105776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `0.0273` n `228`; crypto_major avg `-0.0764` n `8`; equity avg `-0.121` n `67`; fx avg `0.0058` n `6`; index avg `0.0032` n `23`; metal avg `0.0273` n `18`; unknown avg `-0.0178` n `419`
- 1h: commodity avg `0.0175` n `12`; crypto_alt avg `0.0395` n `228`; crypto_major avg `-0.0988` n `8`; equity avg `0.0104` n `67`; fx avg `0.0055` n `6`; index avg `0.1213` n `23`; metal avg `0.0462` n `18`; unknown avg `0.4873` n `419`
- 4h: commodity avg `-0.4702` n `12`; crypto_alt avg `0.1012` n `228`; crypto_major avg `0.0531` n `8`; equity avg `0.3777` n `67`; fx avg `0.0033` n `6`; index avg `0.3422` n `23`; metal avg `0.1387` n `18`; unknown avg `0.0552` n `418`
- 24h: commodity avg `-1.5216` n `12`; crypto_alt avg `-0.2221` n `228`; crypto_major avg `0.0213` n `8`; equity avg `-0.1043` n `67`; fx avg `-0.0615` n `6`; index avg `-0.358` n `23`; metal avg `-1.3071` n `18`; unknown avg `-0.1874` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
