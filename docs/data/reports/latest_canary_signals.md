# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T11:52:30.055758+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `-0.0371` n `234`; crypto_major avg `0.0125` n `8`; equity avg `-0.0028` n `141`; fx avg `-0.0011` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0008` n `20`; unknown avg `1.5971` n `961`
- 1h: commodity avg `-0.0002` n `12`; crypto_alt avg `0.0852` n `234`; crypto_major avg `0.0894` n `8`; equity avg `0.0297` n `141`; fx avg `0.026` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.8126` n `959`
- 4h: commodity avg `-0.0139` n `12`; crypto_alt avg `0.5203` n `234`; crypto_major avg `0.1265` n `8`; equity avg `0.0529` n `141`; fx avg `0.0207` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0067` n `20`; unknown avg `-0.1158` n `943`
- 24h: commodity avg `0.219` n `12`; crypto_alt avg `1.7918` n `234`; crypto_major avg `-0.825` n `8`; equity avg `-0.9299` n `141`; fx avg `0.0018` n `6`; index avg `-0.0158` n `26`; metal avg `-0.0506` n `20`; unknown avg `1120.5368` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
