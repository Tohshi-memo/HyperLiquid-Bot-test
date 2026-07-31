# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T20:22:32.075294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0233` n `12`; crypto_alt avg `0.1418` n `230`; crypto_major avg `0.1843` n `8`; equity avg `-0.0421` n `102`; fx avg `-0.0373` n `6`; index avg `-0.0057` n `25`; metal avg `0.0092` n `20`; unknown avg `-0.0251` n `780`
- 1h: commodity avg `-0.0172` n `12`; crypto_alt avg `0.0504` n `230`; crypto_major avg `-0.072` n `8`; equity avg `-0.6567` n `102`; fx avg `-0.0711` n `6`; index avg `-0.0998` n `25`; metal avg `-0.0567` n `20`; unknown avg `-0.187` n `780`
- 4h: commodity avg `0.1508` n `12`; crypto_alt avg `0.1109` n `230`; crypto_major avg `-0.2093` n `8`; equity avg `0.1401` n `102`; fx avg `0.0243` n `6`; index avg `0.0314` n `25`; metal avg `0.0772` n `20`; unknown avg `7.1106` n `780`
- 24h: commodity avg `0.1674` n `12`; crypto_alt avg `-0.5449` n `230`; crypto_major avg `-2.1439` n `8`; equity avg `-0.8009` n `102`; fx avg `0.157` n `6`; index avg `0.0921` n `25`; metal avg `-0.4198` n `20`; unknown avg `0.2468` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
