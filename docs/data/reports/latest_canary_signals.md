# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T20:37:31.767122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `12`; crypto_alt avg `-0.0317` n `231`; crypto_major avg `-0.0981` n `8`; equity avg `0.0048` n `122`; fx avg `-0.0133` n `6`; index avg `0.0002` n `25`; metal avg `0.0271` n `20`; unknown avg `-0.096` n `793`
- 1h: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.0411` n `231`; crypto_major avg `0.0206` n `8`; equity avg `-0.0271` n `122`; fx avg `-0.0615` n `6`; index avg `-0.0068` n `25`; metal avg `0.0406` n `20`; unknown avg `1.1128` n `793`
- 4h: commodity avg `-0.0324` n `12`; crypto_alt avg `0.3492` n `231`; crypto_major avg `0.047` n `8`; equity avg `0.2434` n `122`; fx avg `-0.0771` n `6`; index avg `0.053` n `25`; metal avg `0.0398` n `20`; unknown avg `0.6926` n `793`
- 24h: commodity avg `-0.0828` n `12`; crypto_alt avg `2.2158` n `231`; crypto_major avg `0.0385` n `8`; equity avg `0.743` n `122`; fx avg `-0.0701` n `6`; index avg `0.1253` n `25`; metal avg `0.1246` n `20`; unknown avg `5.5148` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
