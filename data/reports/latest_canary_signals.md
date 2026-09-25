# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T06:22:27.543480+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0291` n `12`; crypto_alt avg `0.292` n `234`; crypto_major avg `0.0707` n `8`; equity avg `0.1358` n `141`; fx avg `-0.0319` n `6`; index avg `0.0231` n `26`; metal avg `0.0748` n `20`; unknown avg `0.045` n `946`
- 1h: commodity avg `-0.1067` n `12`; crypto_alt avg `0.5198` n `234`; crypto_major avg `0.2142` n `8`; equity avg `0.339` n `141`; fx avg `-0.016` n `6`; index avg `0.0652` n `26`; metal avg `0.1345` n `20`; unknown avg `0.86` n `912`
- 4h: commodity avg `-0.0179` n `12`; crypto_alt avg `-0.2948` n `234`; crypto_major avg `-0.6535` n `8`; equity avg `0.3239` n `141`; fx avg `-0.0599` n `6`; index avg `0.0739` n `26`; metal avg `-0.075` n `20`; unknown avg `1.9591` n `906`
- 24h: commodity avg `0.2682` n `12`; crypto_alt avg `2.0476` n `234`; crypto_major avg `0.4984` n `8`; equity avg `1.0975` n `141`; fx avg `-0.1789` n `6`; index avg `0.1672` n `26`; metal avg `-0.1114` n `20`; unknown avg `13.328` n `799`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
