# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T08:22:33.254709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0318` n `12`; crypto_alt avg `0.0211` n `230`; crypto_major avg `0.0667` n `8`; equity avg `0.1416` n `112`; fx avg `-0.012` n `6`; index avg `-0.0184` n `25`; metal avg `0.0292` n `20`; unknown avg `-0.0014` n `782`
- 1h: commodity avg `0.0176` n `12`; crypto_alt avg `0.0101` n `230`; crypto_major avg `0.0347` n `8`; equity avg `0.3973` n `112`; fx avg `-0.0092` n `6`; index avg `0.0226` n `25`; metal avg `0.1035` n `20`; unknown avg `0.0243` n `782`
- 4h: commodity avg `-0.0764` n `12`; crypto_alt avg `0.2856` n `230`; crypto_major avg `0.1541` n `8`; equity avg `0.8393` n `112`; fx avg `-0.0339` n `6`; index avg `0.0936` n `25`; metal avg `0.3609` n `20`; unknown avg `0.0056` n `766`
- 24h: commodity avg `0.489` n `12`; crypto_alt avg `0.2617` n `230`; crypto_major avg `-0.7902` n `8`; equity avg `2.0458` n `109`; fx avg `-0.0959` n `6`; index avg `0.0626` n `25`; metal avg `0.3925` n `20`; unknown avg `110.8263` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
