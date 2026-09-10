# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T20:52:36.029704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0413` n `12`; crypto_alt avg `-0.0245` n `233`; crypto_major avg `-0.0211` n `8`; equity avg `-0.009` n `136`; fx avg `-0.0162` n `6`; index avg `-0.0008` n `26`; metal avg `0.0062` n `20`; unknown avg `11.6492` n `778`
- 1h: commodity avg `0.1917` n `12`; crypto_alt avg `0.2968` n `233`; crypto_major avg `0.23` n `8`; equity avg `0.0087` n `136`; fx avg `-0.0065` n `6`; index avg `0.0081` n `26`; metal avg `0.0045` n `20`; unknown avg `12.0541` n `750`
- 4h: commodity avg `0.4344` n `12`; crypto_alt avg `0.5384` n `233`; crypto_major avg `0.6008` n `8`; equity avg `-0.4989` n `136`; fx avg `-0.0011` n `6`; index avg `-0.0472` n `26`; metal avg `-0.2217` n `20`; unknown avg `5.7825` n `749`
- 24h: commodity avg `1.2074` n `12`; crypto_alt avg `-3.0106` n `233`; crypto_major avg `-2.2208` n `8`; equity avg `-2.1155` n `136`; fx avg `0.1051` n `6`; index avg `-0.3243` n `26`; metal avg `-1.2556` n `20`; unknown avg `-1.2635` n `667`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
