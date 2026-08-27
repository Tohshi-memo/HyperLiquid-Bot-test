# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T21:07:25.102941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `0.1976` n `231`; crypto_major avg `0.1126` n `8`; equity avg `-0.0389` n `127`; fx avg `-0.0067` n `6`; index avg `0.0059` n `26`; metal avg `-0.0101` n `20`; unknown avg `0.0431` n `792`
- 1h: commodity avg `-0.0389` n `12`; crypto_alt avg `0.3705` n `231`; crypto_major avg `0.151` n `8`; equity avg `-0.2141` n `127`; fx avg `-0.0104` n `6`; index avg `-0.0184` n `26`; metal avg `-0.0223` n `20`; unknown avg `-0.0398` n `792`
- 4h: commodity avg `0.0416` n `12`; crypto_alt avg `-0.4798` n `231`; crypto_major avg `-0.3332` n `8`; equity avg `0.0613` n `127`; fx avg `0.0055` n `6`; index avg `-0.0093` n `26`; metal avg `0.0231` n `20`; unknown avg `0.1948` n `792`
- 24h: commodity avg `0.3247` n `12`; crypto_alt avg `2.8401` n `231`; crypto_major avg `3.8203` n `8`; equity avg `0.511` n `127`; fx avg `-0.0303` n `6`; index avg `0.0505` n `26`; metal avg `0.2232` n `20`; unknown avg `1.0639` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
