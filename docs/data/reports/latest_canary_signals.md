# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T13:37:37.459687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0903` n `12`; crypto_alt avg `0.9445` n `228`; crypto_major avg `1.0178` n `8`; equity avg `0.5373` n `73`; fx avg `-0.0222` n `6`; index avg `0.2553` n `23`; metal avg `0.0008` n `18`; unknown avg `0.1896` n `425`
- 1h: commodity avg `0.0649` n `12`; crypto_alt avg `0.1196` n `228`; crypto_major avg `-0.1711` n `8`; equity avg `0.4832` n `73`; fx avg `-0.0188` n `6`; index avg `0.2679` n `23`; metal avg `0.1577` n `18`; unknown avg `-0.1427` n `425`
- 4h: commodity avg `-0.1335` n `12`; crypto_alt avg `2.2861` n `228`; crypto_major avg `1.6715` n `8`; equity avg `0.8864` n `73`; fx avg `-0.0036` n `6`; index avg `0.1575` n `23`; metal avg `0.8638` n `18`; unknown avg `0.3543` n `422`
- 24h: commodity avg `-0.3331` n `12`; crypto_alt avg `-6.3395` n `228`; crypto_major avg `-4.7737` n `8`; equity avg `-2.583` n `73`; fx avg `0.0882` n `6`; index avg `-0.9386` n `23`; metal avg `0.3889` n `18`; unknown avg `-1.2864` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
