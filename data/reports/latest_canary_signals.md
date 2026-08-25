# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T16:52:50.045357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `0.116` n `231`; crypto_major avg `0.0915` n `8`; equity avg `-0.0829` n `122`; fx avg `-0.0097` n `6`; index avg `-0.0125` n `25`; metal avg `0.0174` n `20`; unknown avg `0.0919` n `795`
- 1h: commodity avg `0.1056` n `12`; crypto_alt avg `0.2761` n `231`; crypto_major avg `0.1081` n `8`; equity avg `-0.0184` n `122`; fx avg `-0.0116` n `6`; index avg `0.0083` n `25`; metal avg `0.0207` n `20`; unknown avg `0.0653` n `795`
- 4h: commodity avg `0.1503` n `12`; crypto_alt avg `-0.215` n `231`; crypto_major avg `0.0725` n `8`; equity avg `0.3807` n `122`; fx avg `0.0006` n `6`; index avg `-0.039` n `25`; metal avg `0.1618` n `20`; unknown avg `0.0115` n `795`
- 24h: commodity avg `-0.6637` n `12`; crypto_alt avg `-1.2059` n `231`; crypto_major avg `-0.0387` n `8`; equity avg `1.5459` n `122`; fx avg `0.0258` n `6`; index avg `0.185` n `25`; metal avg `-0.109` n `20`; unknown avg `-0.7414` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
