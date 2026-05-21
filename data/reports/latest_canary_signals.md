# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T07:52:17.798581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0253` n `12`; crypto_alt avg `0.1244` n `228`; crypto_major avg `0.2574` n `8`; equity avg `0.0994` n `66`; fx avg `-0.0009` n `6`; index avg `0.1187` n `23`; metal avg `0.0804` n `18`; unknown avg `1.2634` n `385`
- 1h: commodity avg `-0.0781` n `12`; crypto_alt avg `0.4369` n `228`; crypto_major avg `0.706` n `8`; equity avg `0.002` n `66`; fx avg `-0.0372` n `6`; index avg `0.0321` n `23`; metal avg `0.0495` n `18`; unknown avg `1.9497` n `385`
- 4h: commodity avg `0.1504` n `12`; crypto_alt avg `-0.0691` n `228`; crypto_major avg `0.1347` n `8`; equity avg `-0.2` n `66`; fx avg `-0.0279` n `6`; index avg `-0.0764` n `23`; metal avg `-0.402` n `18`; unknown avg `1.7531` n `374`
- 24h: commodity avg `-1.7694` n `12`; crypto_alt avg `2.7211` n `228`; crypto_major avg `3.4651` n `8`; equity avg `1.7163` n `66`; fx avg `0.0442` n `6`; index avg `1.3921` n `23`; metal avg `0.2143` n `18`; unknown avg `6.4056` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
