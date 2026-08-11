# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T15:52:42.985614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.13` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `-0.0525` n `230`; crypto_major avg `-0.0833` n `8`; equity avg `-0.0783` n `113`; fx avg `0.0005` n `6`; index avg `-0.0135` n `25`; metal avg `0.023` n `20`; unknown avg `-0.0412` n `785`
- 1h: commodity avg `0.144` n `12`; crypto_alt avg `-0.9759` n `230`; crypto_major avg `-0.4722` n `8`; equity avg `-0.4175` n `113`; fx avg `0.0123` n `6`; index avg `-0.0967` n `25`; metal avg `-0.1242` n `20`; unknown avg `-0.1892` n `785`
- 4h: commodity avg `0.1966` n `12`; crypto_alt avg `-1.7117` n `230`; crypto_major avg `-1.1771` n `8`; equity avg `0.131` n `113`; fx avg `0.0376` n `6`; index avg `-0.0471` n `25`; metal avg `-0.2319` n `20`; unknown avg `0.182` n `785`
- 24h: commodity avg `0.243` n `12`; crypto_alt avg `-2.3176` n `230`; crypto_major avg `-0.7272` n `8`; equity avg `-0.0333` n `113`; fx avg `-0.0541` n `6`; index avg `0.0644` n `25`; metal avg `0.0449` n `20`; unknown avg `-0.3178` n `753`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1978`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
