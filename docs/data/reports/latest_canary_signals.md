# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T15:52:31.651546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.9683` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.729` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- polymarket_volume_spike: score `2.32` - Polymarket crypto volume is unusually high.
- 1h_crypto_equity_divergence: score `-1.772` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1369` n `13`; crypto_alt avg `-0.5806` n `239`; crypto_major avg `-0.7837` n `8`; equity avg `-0.9212` n `166`; fx avg `-0.0188` n `6`; index avg `-0.0994` n `27`; metal avg `-0.0998` n `20`; unknown avg `6.8456` n `1264`
- 1h: commodity avg `-0.587` n `13`; crypto_alt avg `-0.506` n `239`; crypto_major avg `-0.233` n `8`; equity avg `1.539` n `166`; fx avg `-0.0609` n `6`; index avg `0.106` n `27`; metal avg `-0.0875` n `20`; unknown avg `7.1076` n `1262`
- 4h: commodity avg `-0.8179` n `13`; crypto_alt avg `2.3743` n `239`; crypto_major avg `3.1504` n `8`; equity avg `4.6015` n `166`; fx avg `-0.1914` n `6`; index avg `0.494` n `27`; metal avg `0.4214` n `20`; unknown avg `215.3628` n `1250`
- 24h: commodity avg `-1.6363` n `13`; crypto_alt avg `3.2656` n `239`; crypto_major avg `4.3847` n `8`; equity avg `6.858` n `166`; fx avg `-0.0245` n `6`; index avg `0.6058` n `27`; metal avg `0.8005` n `20`; unknown avg `10.1056` n `1057`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
