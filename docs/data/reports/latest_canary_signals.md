# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T06:52:25.487957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6193` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5828` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.059` n `12`; crypto_alt avg `0.0709` n `228`; crypto_major avg `0.1152` n `8`; equity avg `0.2114` n `86`; fx avg `-0.0085` n `6`; index avg `0.0843` n `23`; metal avg `0.0454` n `20`; unknown avg `-0.0225` n `716`
- 1h: commodity avg `-0.0225` n `12`; crypto_alt avg `-1.4003` n `228`; crypto_major avg `-0.8978` n `8`; equity avg `-0.2659` n `86`; fx avg `0.066` n `6`; index avg `-0.1566` n `23`; metal avg `-0.1264` n `20`; unknown avg `-0.435` n `684`
- 4h: commodity avg `-0.1353` n `12`; crypto_alt avg `-2.0487` n `228`; crypto_major avg `-2.0919` n `8`; equity avg `-1.7986` n `86`; fx avg `0.0235` n `6`; index avg `-0.4726` n `23`; metal avg `-0.5091` n `20`; unknown avg `-0.0868` n `676`
- 24h: commodity avg `-0.6272` n `12`; crypto_alt avg `-2.6256` n `228`; crypto_major avg `-2.0994` n `8`; equity avg `-3.9679` n `85`; fx avg `0.0216` n `6`; index avg `-0.7813` n `23`; metal avg `-1.5691` n `18`; unknown avg `0.5832` n `647`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
