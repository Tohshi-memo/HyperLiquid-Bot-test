# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T06:07:26.153808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0059` n `12`; crypto_alt avg `-0.0792` n `229`; crypto_major avg `-0.1388` n `8`; equity avg `-0.0733` n `91`; fx avg `-0.066` n `6`; index avg `-0.0439` n `25`; metal avg `0.0224` n `20`; unknown avg `-0.0273` n `733`
- 1h: commodity avg `-0.087` n `12`; crypto_alt avg `-0.0384` n `229`; crypto_major avg `0.0667` n `8`; equity avg `-0.2502` n `91`; fx avg `-0.0886` n `6`; index avg `-0.0548` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.0015` n `733`
- 4h: commodity avg `-0.055` n `12`; crypto_alt avg `0.0087` n `229`; crypto_major avg `0.2901` n `8`; equity avg `-0.2972` n `91`; fx avg `-0.0906` n `6`; index avg `-0.0503` n `25`; metal avg `0.0786` n `20`; unknown avg `0.027` n `733`
- 24h: commodity avg `-0.8924` n `12`; crypto_alt avg `0.8776` n `229`; crypto_major avg `1.1067` n `8`; equity avg `1.0744` n `91`; fx avg `-0.067` n `6`; index avg `0.2967` n `25`; metal avg `0.6181` n `20`; unknown avg `0.0853` n `732`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
