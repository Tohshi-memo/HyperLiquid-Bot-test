# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T10:07:25.856566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0005` n `12`; crypto_alt avg `-0.1154` n `231`; crypto_major avg `-0.1655` n `8`; equity avg `-0.0065` n `127`; fx avg `0.0019` n `6`; index avg `0.0006` n `26`; metal avg `0.0086` n `20`; unknown avg `-0.0109` n `793`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `0.0173` n `231`; crypto_major avg `-0.0541` n `8`; equity avg `0.0096` n `127`; fx avg `-0.0115` n `6`; index avg `-0.0084` n `26`; metal avg `0.0044` n `20`; unknown avg `-0.0178` n `791`
- 4h: commodity avg `0.0437` n `12`; crypto_alt avg `-0.4893` n `231`; crypto_major avg `-0.2359` n `8`; equity avg `0.0339` n `127`; fx avg `-0.0137` n `6`; index avg `-0.0143` n `26`; metal avg `0.0168` n `20`; unknown avg `0.0322` n `791`
- 24h: commodity avg `-0.0247` n `12`; crypto_alt avg `-1.5538` n `231`; crypto_major avg `-1.5561` n `8`; equity avg `-1.2561` n `127`; fx avg `-0.0238` n `6`; index avg `-0.1374` n `26`; metal avg `-0.7291` n `20`; unknown avg `-0.3419` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1874`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
