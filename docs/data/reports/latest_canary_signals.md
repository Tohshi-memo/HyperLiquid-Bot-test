# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T13:22:32.540918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.34` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1004` n `13`; crypto_alt avg `-0.0383` n `235`; crypto_major avg `-0.0542` n `8`; equity avg `0.0153` n `143`; fx avg `0.0268` n `6`; index avg `-0.0117` n `26`; metal avg `-0.1657` n `20`; unknown avg `21.0836` n `984`
- 1h: commodity avg `0.0948` n `13`; crypto_alt avg `0.4041` n `235`; crypto_major avg `0.1743` n `8`; equity avg `0.7182` n `142`; fx avg `-0.0112` n `6`; index avg `0.1723` n `26`; metal avg `0.0711` n `20`; unknown avg `6.6466` n `982`
- 4h: commodity avg `0.1658` n `13`; crypto_alt avg `0.5878` n `235`; crypto_major avg `0.3549` n `8`; equity avg `0.3965` n `142`; fx avg `-0.03` n `6`; index avg `0.1678` n `26`; metal avg `-0.0278` n `20`; unknown avg `-0.0605` n `974`
- 24h: commodity avg `-0.4102` n `13`; crypto_alt avg `3.2099` n `235`; crypto_major avg `2.7809` n `8`; equity avg `1.8642` n `142`; fx avg `-0.3261` n `6`; index avg `0.4092` n `26`; metal avg `0.0112` n `20`; unknown avg `0.3694` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1728`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
