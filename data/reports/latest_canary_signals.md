# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T09:22:36.353157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0359` n `12`; crypto_alt avg `0.1097` n `230`; crypto_major avg `0.0854` n `8`; equity avg `0.1797` n `113`; fx avg `-0.0042` n `6`; index avg `0.0286` n `25`; metal avg `0.0362` n `20`; unknown avg `0.0522` n `785`
- 1h: commodity avg `-0.0115` n `12`; crypto_alt avg `0.1515` n `230`; crypto_major avg `0.2837` n `8`; equity avg `-0.0199` n `113`; fx avg `-0.0057` n `6`; index avg `0.0233` n `25`; metal avg `0.1107` n `20`; unknown avg `0.0736` n `785`
- 4h: commodity avg `0.3309` n `12`; crypto_alt avg `-0.1278` n `230`; crypto_major avg `0.2509` n `8`; equity avg `-0.3892` n `113`; fx avg `0.0192` n `6`; index avg `-0.0446` n `25`; metal avg `-0.0429` n `20`; unknown avg `0.0858` n `753`
- 24h: commodity avg `1.1345` n `12`; crypto_alt avg `-1.1388` n `230`; crypto_major avg `-0.7517` n `8`; equity avg `-1.5327` n `113`; fx avg `0.0071` n `6`; index avg `-0.0463` n `25`; metal avg `0.2762` n `20`; unknown avg `0.1449` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1713`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
