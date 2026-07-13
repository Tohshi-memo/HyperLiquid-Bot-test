# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T06:37:25.628415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0562` n `12`; crypto_alt avg `0.0549` n `230`; crypto_major avg `0.0101` n `8`; equity avg `-0.0759` n `92`; fx avg `-0.0268` n `6`; index avg `0.0309` n `25`; metal avg `0.0648` n `20`; unknown avg `0.1421` n `766`
- 1h: commodity avg `-0.1115` n `12`; crypto_alt avg `0.0789` n `230`; crypto_major avg `-0.2091` n `8`; equity avg `-0.3237` n `92`; fx avg `-0.014` n `6`; index avg `-0.0317` n `25`; metal avg `-0.0024` n `20`; unknown avg `-0.0414` n `750`
- 4h: commodity avg `-0.0805` n `12`; crypto_alt avg `-0.4077` n `230`; crypto_major avg `-1.0947` n `8`; equity avg `-1.1583` n `92`; fx avg `-0.0044` n `6`; index avg `-0.2134` n `25`; metal avg `-0.0996` n `20`; unknown avg `-0.1817` n `750`
- 24h: commodity avg `0.0633` n `12`; crypto_alt avg `-1.1608` n `230`; crypto_major avg `-0.9559` n `8`; equity avg `-2.5269` n `92`; fx avg `0.0132` n `6`; index avg `-0.5182` n `25`; metal avg `-0.3999` n `20`; unknown avg `-0.0432` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
