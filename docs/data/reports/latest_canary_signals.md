# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T15:22:35.018980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2148` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1065` n `12`; crypto_alt avg `-0.2396` n `230`; crypto_major avg `-0.1901` n `8`; equity avg `-0.2664` n `100`; fx avg `-0.0127` n `6`; index avg `-0.0668` n `25`; metal avg `-0.1144` n `20`; unknown avg `-0.084` n `772`
- 1h: commodity avg `0.1633` n `12`; crypto_alt avg `-0.6299` n `230`; crypto_major avg `-0.6457` n `8`; equity avg `-1.4063` n `100`; fx avg `-0.0236` n `6`; index avg `-0.1759` n `25`; metal avg `-0.1337` n `20`; unknown avg `-0.1103` n `772`
- 4h: commodity avg `0.3242` n `12`; crypto_alt avg `-1.009` n `230`; crypto_major avg `-1.6441` n `8`; equity avg `-1.8755` n `99`; fx avg `-0.0187` n `6`; index avg `-0.4293` n `25`; metal avg `-0.427` n `20`; unknown avg `0.1276` n `772`
- 24h: commodity avg `1.0856` n `12`; crypto_alt avg `-1.6325` n `230`; crypto_major avg `-2.1091` n `8`; equity avg `-2.4855` n `99`; fx avg `-0.0937` n `6`; index avg `-0.4781` n `25`; metal avg `-1.0041` n `20`; unknown avg `-0.2687` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
