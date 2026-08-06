# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T12:37:31.311013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0332` n `12`; crypto_alt avg `0.0175` n `230`; crypto_major avg `0.0059` n `8`; equity avg `0.05` n `109`; fx avg `0.016` n `6`; index avg `0.0183` n `25`; metal avg `0.0281` n `20`; unknown avg `0.0184` n `781`
- 1h: commodity avg `0.0806` n `12`; crypto_alt avg `-0.0289` n `230`; crypto_major avg `-0.1716` n `8`; equity avg `-0.302` n `109`; fx avg `0.0082` n `6`; index avg `-0.0421` n `25`; metal avg `-0.0548` n `20`; unknown avg `-0.02` n `781`
- 4h: commodity avg `0.1564` n `12`; crypto_alt avg `-0.2204` n `230`; crypto_major avg `-0.5585` n `8`; equity avg `-0.3525` n `109`; fx avg `-0.0063` n `6`; index avg `-0.071` n `25`; metal avg `-0.027` n `20`; unknown avg `108.1888` n `781`
- 24h: commodity avg `-0.0856` n `12`; crypto_alt avg `-0.0824` n `230`; crypto_major avg `-0.9387` n `8`; equity avg `-1.9793` n `109`; fx avg `0.016` n `6`; index avg `-0.434` n `25`; metal avg `0.2683` n `20`; unknown avg `113.0914` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
