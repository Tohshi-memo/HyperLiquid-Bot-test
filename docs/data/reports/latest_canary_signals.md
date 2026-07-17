# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T17:07:26.704163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.032` n `12`; crypto_alt avg `0.2028` n `230`; crypto_major avg `0.2864` n `8`; equity avg `0.3418` n `96`; fx avg `0.0059` n `6`; index avg `0.0574` n `25`; metal avg `0.0155` n `20`; unknown avg `-0.0519` n `769`
- 1h: commodity avg `0.0814` n `12`; crypto_alt avg `0.4261` n `230`; crypto_major avg `0.5789` n `8`; equity avg `0.8446` n `96`; fx avg `0.0362` n `6`; index avg `0.1261` n `25`; metal avg `0.0632` n `20`; unknown avg `0.3215` n `769`
- 4h: commodity avg `0.1842` n `12`; crypto_alt avg `1.6158` n `230`; crypto_major avg `1.5452` n `8`; equity avg `3.0283` n `96`; fx avg `0.104` n `6`; index avg `0.4283` n `25`; metal avg `0.4091` n `20`; unknown avg `0.6394` n `769`
- 24h: commodity avg `0.7807` n `12`; crypto_alt avg `-1.1453` n `230`; crypto_major avg `-1.5119` n `8`; equity avg `-0.5416` n `94`; fx avg `0.1167` n `6`; index avg `-0.1451` n `25`; metal avg `-0.1124` n `20`; unknown avg `-0.2157` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
