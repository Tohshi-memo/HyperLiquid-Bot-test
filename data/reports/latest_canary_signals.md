# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T04:37:28.297736+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.63` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.6602` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0248` n `13`; crypto_alt avg `-0.5604` n `239`; crypto_major avg `-0.3156` n `8`; equity avg `-0.1968` n `158`; fx avg `0.0049` n `6`; index avg `-0.0426` n `27`; metal avg `-0.0387` n `20`; unknown avg `4.428` n `1264`
- 1h: commodity avg `-0.075` n `13`; crypto_alt avg `0.1014` n `239`; crypto_major avg `0.1292` n `8`; equity avg `-0.1663` n `158`; fx avg `0.0011` n `6`; index avg `-0.0117` n `27`; metal avg `0.03` n `20`; unknown avg `-0.0757` n `1252`
- 4h: commodity avg `-0.4254` n `13`; crypto_alt avg `-0.6619` n `239`; crypto_major avg `-0.5166` n `8`; equity avg `-2.1768` n `158`; fx avg `-0.0787` n `6`; index avg `-0.4131` n `27`; metal avg `-0.1082` n `20`; unknown avg `0.3477` n `1254`
- 24h: commodity avg `-0.2681` n `13`; crypto_alt avg `-0.6758` n `239`; crypto_major avg `-0.7475` n `8`; equity avg `-1.0783` n `158`; fx avg `0.1175` n `6`; index avg `-0.3564` n `27`; metal avg `-0.3565` n `20`; unknown avg `-0.3938` n `1049`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
