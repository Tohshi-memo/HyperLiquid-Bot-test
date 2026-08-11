# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T06:37:35.918981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1458` n `12`; crypto_alt avg `-0.0707` n `230`; crypto_major avg `-0.1787` n `8`; equity avg `-0.164` n `113`; fx avg `0.0011` n `6`; index avg `-0.0279` n `25`; metal avg `-0.0666` n `20`; unknown avg `-0.0254` n `785`
- 1h: commodity avg `0.2669` n `12`; crypto_alt avg `-0.1765` n `230`; crypto_major avg `-0.2428` n `8`; equity avg `-0.2853` n `113`; fx avg `0.0177` n `6`; index avg `-0.0581` n `25`; metal avg `-0.0577` n `20`; unknown avg `-0.0215` n `753`
- 4h: commodity avg `0.2524` n `12`; crypto_alt avg `-0.3543` n `230`; crypto_major avg `-0.2414` n `8`; equity avg `-0.2692` n `113`; fx avg `0.0014` n `6`; index avg `-0.0328` n `25`; metal avg `-0.37` n `20`; unknown avg `-0.0202` n `753`
- 24h: commodity avg `1.2296` n `12`; crypto_alt avg `-1.0626` n `230`; crypto_major avg `-0.9982` n `8`; equity avg `-1.3722` n `113`; fx avg `0.0466` n `6`; index avg `-0.0388` n `25`; metal avg `0.031` n `20`; unknown avg `0.1524` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
