# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T05:22:25.190844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `0.3554` n `231`; crypto_major avg `0.2403` n `8`; equity avg `-0.0919` n `122`; fx avg `-0.0095` n `6`; index avg `-0.0074` n `25`; metal avg `-0.0331` n `20`; unknown avg `-0.2019` n `793`
- 1h: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.0523` n `231`; crypto_major avg `-0.1506` n `8`; equity avg `-0.1061` n `122`; fx avg `-0.0281` n `6`; index avg `0.0095` n `25`; metal avg `-0.0007` n `20`; unknown avg `0.1549` n `793`
- 4h: commodity avg `0.1489` n `12`; crypto_alt avg `-0.278` n `231`; crypto_major avg `-0.3516` n `8`; equity avg `-1.4507` n `122`; fx avg `-0.0472` n `6`; index avg `-0.1554` n `25`; metal avg `0.0653` n `20`; unknown avg `0.1257` n `793`
- 24h: commodity avg `-0.2776` n `12`; crypto_alt avg `4.2951` n `231`; crypto_major avg `1.5008` n `8`; equity avg `-1.0555` n `122`; fx avg `-0.2252` n `6`; index avg `-0.0893` n `25`; metal avg `0.1075` n `20`; unknown avg `5.873` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
