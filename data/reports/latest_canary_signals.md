# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T00:52:30.111087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2338` n `12`; crypto_alt avg `0.0766` n `234`; crypto_major avg `0.2413` n `8`; equity avg `0.0297` n `141`; fx avg `0.0061` n `6`; index avg `0.0211` n `26`; metal avg `0.0125` n `20`; unknown avg `0.1899` n `960`
- 1h: commodity avg `0.3527` n `12`; crypto_alt avg `-0.4715` n `234`; crypto_major avg `-0.3185` n `8`; equity avg `-0.1885` n `141`; fx avg `0.0045` n `6`; index avg `-0.0728` n `26`; metal avg `-0.0288` n `20`; unknown avg `0.1746` n `952`
- 4h: commodity avg `0.3767` n `12`; crypto_alt avg `0.0941` n `234`; crypto_major avg `0.003` n `8`; equity avg `-0.1766` n `141`; fx avg `-0.008` n `6`; index avg `-0.0561` n `26`; metal avg `-0.0418` n `20`; unknown avg `-0.0051` n `926`
- 24h: commodity avg `0.0643` n `12`; crypto_alt avg `2.5835` n `234`; crypto_major avg `0.7911` n `8`; equity avg `-0.0978` n `141`; fx avg `-0.2264` n `6`; index avg `0.1914` n `26`; metal avg `0.1915` n `20`; unknown avg `1125.9747` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
