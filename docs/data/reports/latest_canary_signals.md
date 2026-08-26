# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T03:52:24.825181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `-0.0449` n `231`; crypto_major avg `-0.0802` n `8`; equity avg `0.1633` n `122`; fx avg `-0.0008` n `6`; index avg `0.042` n `25`; metal avg `-0.0396` n `20`; unknown avg `0.0141` n `797`
- 1h: commodity avg `-0.0095` n `12`; crypto_alt avg `-0.3425` n `231`; crypto_major avg `-0.2258` n `8`; equity avg `0.15` n `122`; fx avg `-0.0114` n `6`; index avg `0.0377` n `25`; metal avg `-0.1084` n `20`; unknown avg `-0.0439` n `797`
- 4h: commodity avg `-0.1424` n `12`; crypto_alt avg `1.088` n `231`; crypto_major avg `0.7364` n `8`; equity avg `0.3499` n `122`; fx avg `0.004` n `6`; index avg `0.1308` n `25`; metal avg `0.0902` n `20`; unknown avg `0.7529` n `796`
- 24h: commodity avg `-0.894` n `12`; crypto_alt avg `-2.539` n `231`; crypto_major avg `-2.5653` n `8`; equity avg `1.6512` n `122`; fx avg `0.0097` n `6`; index avg `0.2685` n `25`; metal avg `0.2729` n `20`; unknown avg `0.167` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
