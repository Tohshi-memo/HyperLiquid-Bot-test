# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T07:37:29.467881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0122` n `13`; crypto_alt avg `0.0273` n `236`; crypto_major avg `0.1004` n `8`; equity avg `0.0456` n `151`; fx avg `0.0022` n `6`; index avg `0.011` n `26`; metal avg `0.0035` n `20`; unknown avg `0.5198` n `1193`
- 1h: commodity avg `-0.1629` n `13`; crypto_alt avg `-0.187` n `236`; crypto_major avg `0.183` n `8`; equity avg `-0.018` n `151`; fx avg `0.0037` n `6`; index avg `0.0016` n `26`; metal avg `-0.0042` n `20`; unknown avg `0.1899` n `1189`
- 4h: commodity avg `-0.234` n `13`; crypto_alt avg `-0.4369` n `236`; crypto_major avg `0.1719` n `8`; equity avg `0.03` n `151`; fx avg `0.0007` n `6`; index avg `0.0325` n `26`; metal avg `-0.0034` n `20`; unknown avg `0.688` n `1167`
- 24h: commodity avg `0.2839` n `13`; crypto_alt avg `-1.9539` n `236`; crypto_major avg `-1.0622` n `8`; equity avg `-3.8107` n `151`; fx avg `0.06` n `6`; index avg `-0.5919` n `26`; metal avg `-0.2764` n `20`; unknown avg `40.6002` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.18`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1446`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.126`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1242`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0763`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
