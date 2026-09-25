# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T16:22:28.531935+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0232` n `12`; crypto_alt avg `0.0671` n `234`; crypto_major avg `-0.0937` n `8`; equity avg `-0.1634` n `141`; fx avg `-0.0022` n `6`; index avg `-0.0397` n `26`; metal avg `-0.0584` n `20`; unknown avg `0.2008` n `956`
- 1h: commodity avg `-0.3472` n `12`; crypto_alt avg `0.1243` n `234`; crypto_major avg `-0.1897` n `8`; equity avg `0.19` n `141`; fx avg `-0.0295` n `6`; index avg `0.0731` n `26`; metal avg `0.0927` n `20`; unknown avg `0.1788` n `930`
- 4h: commodity avg `-0.3065` n `12`; crypto_alt avg `0.1714` n `234`; crypto_major avg `-0.4226` n `8`; equity avg `-0.601` n `141`; fx avg `-0.0673` n `6`; index avg `0.0029` n `26`; metal avg `-0.0547` n `20`; unknown avg `9.9393` n `894`
- 24h: commodity avg `-0.7904` n `12`; crypto_alt avg `1.3` n `234`; crypto_major avg `0.3109` n `8`; equity avg `0.2809` n `141`; fx avg `-0.2688` n `6`; index avg `0.1643` n `26`; metal avg `0.1331` n `20`; unknown avg `1604.7935` n `805`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
