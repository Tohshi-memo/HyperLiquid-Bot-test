# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T08:37:29.664224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.0423` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `0.4135` n `231`; crypto_major avg `0.3951` n `8`; equity avg `0.0434` n `127`; fx avg `0.0101` n `6`; index avg `0.0143` n `26`; metal avg `-0.0225` n `20`; unknown avg `0.0087` n `792`
- 1h: commodity avg `0.0509` n `12`; crypto_alt avg `1.32` n `231`; crypto_major avg `1.359` n `8`; equity avg `0.5042` n `127`; fx avg `-0.0114` n `6`; index avg `0.069` n `26`; metal avg `0.021` n `20`; unknown avg `0.1236` n `791`
- 4h: commodity avg `-0.1045` n `12`; crypto_alt avg `1.6662` n `231`; crypto_major avg `1.8556` n `8`; equity avg `0.6819` n `127`; fx avg `-0.0091` n `6`; index avg `0.0588` n `26`; metal avg `-0.1867` n `20`; unknown avg `0.2576` n `775`
- 24h: commodity avg `0.4628` n `12`; crypto_alt avg `1.5379` n `231`; crypto_major avg `1.9303` n `8`; equity avg `2.0339` n `127`; fx avg `-0.0977` n `6`; index avg `0.3155` n `26`; metal avg `-0.3526` n `20`; unknown avg `0.506` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
