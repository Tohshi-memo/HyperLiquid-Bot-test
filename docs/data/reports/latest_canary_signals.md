# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T06:44:53.888821+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `0.0088` n `233`; crypto_major avg `-0.1037` n `8`; equity avg `-0.1064` n `136`; fx avg `-0.0053` n `6`; index avg `-0.0176` n `26`; metal avg `0.0037` n `20`; unknown avg `-0.0273` n `838`
- 1h: commodity avg `0.0274` n `12`; crypto_alt avg `-0.0698` n `233`; crypto_major avg `-0.2453` n `8`; equity avg `-0.1951` n `136`; fx avg `-0.006` n `6`; index avg `-0.0328` n `26`; metal avg `0.0023` n `20`; unknown avg `-0.022` n `812`
- 4h: commodity avg `0.0833` n `12`; crypto_alt avg `0.1348` n `233`; crypto_major avg `-0.3028` n `8`; equity avg `-0.4015` n `136`; fx avg `-0.0099` n `6`; index avg `-0.0774` n `26`; metal avg `0.0062` n `20`; unknown avg `-0.0449` n `804`
- 24h: commodity avg `0.1624` n `12`; crypto_alt avg `0.8316` n `233`; crypto_major avg `-0.1047` n `8`; equity avg `-0.7474` n `136`; fx avg `-0.012` n `6`; index avg `-0.124` n `26`; metal avg `0.0326` n `20`; unknown avg `0.4776` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
