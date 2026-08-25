# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T23:37:41.637730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0126` n `12`; crypto_alt avg `-0.0897` n `231`; crypto_major avg `-0.0814` n `8`; equity avg `-0.0657` n `122`; fx avg `-0.0107` n `6`; index avg `-0.0086` n `25`; metal avg `-0.01` n `20`; unknown avg `-0.1135` n `795`
- 1h: commodity avg `0.0334` n `12`; crypto_alt avg `-0.282` n `231`; crypto_major avg `-0.2964` n `8`; equity avg `-0.1134` n `122`; fx avg `-0.0086` n `6`; index avg `-0.0269` n `25`; metal avg `-0.0574` n `20`; unknown avg `-0.1687` n `795`
- 4h: commodity avg `-0.1866` n `12`; crypto_alt avg `-0.7836` n `231`; crypto_major avg `-0.8324` n `8`; equity avg `0.1251` n `122`; fx avg `-0.0014` n `6`; index avg `0.0193` n `25`; metal avg `-0.0139` n `20`; unknown avg `-0.246` n `795`
- 24h: commodity avg `-0.7003` n `12`; crypto_alt avg `-2.0871` n `231`; crypto_major avg `-1.3398` n `8`; equity avg `2.073` n `122`; fx avg `0.0425` n `6`; index avg `0.249` n `25`; metal avg `-0.1883` n `20`; unknown avg `-0.5236` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
