# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T13:07:25.220199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.1932` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.7458` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0799` n `12`; crypto_alt avg `-0.1367` n `231`; crypto_major avg `0.0061` n `8`; equity avg `-0.1444` n `122`; fx avg `0.0185` n `6`; index avg `-0.0225` n `25`; metal avg `0.0738` n `20`; unknown avg `0.5349` n `793`
- 1h: commodity avg `0.1229` n `12`; crypto_alt avg `0.7623` n `231`; crypto_major avg `0.8846` n `8`; equity avg `-0.0678` n `122`; fx avg `0.0011` n `6`; index avg `-0.0357` n `25`; metal avg `0.145` n `20`; unknown avg `0.5319` n `793`
- 4h: commodity avg `0.3625` n `12`; crypto_alt avg `1.4542` n `231`; crypto_major avg `1.9776` n `8`; equity avg `-0.2156` n `122`; fx avg `0.0084` n `6`; index avg `-0.0483` n `25`; metal avg `0.2318` n `20`; unknown avg `1.1775` n `793`
- 24h: commodity avg `0.0845` n `12`; crypto_alt avg `1.4758` n `231`; crypto_major avg `1.2489` n `8`; equity avg `-1.6189` n `122`; fx avg `-0.1234` n `6`; index avg `-0.1745` n `25`; metal avg `0.3035` n `20`; unknown avg `4.3201` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
