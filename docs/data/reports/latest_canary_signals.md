# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T02:37:29.578497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.5244` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-2.056` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.9582` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0442` n `12`; crypto_alt avg `-0.0712` n `229`; crypto_major avg `-0.1543` n `8`; equity avg `-0.0449` n `91`; fx avg `0.0023` n `6`; index avg `-0.0224` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.4282` n `763`
- 1h: commodity avg `0.064` n `12`; crypto_alt avg `-0.3108` n `229`; crypto_major avg `-0.3616` n `8`; equity avg `0.0414` n `91`; fx avg `-0.0028` n `6`; index avg `-0.0725` n `25`; metal avg `0.1738` n `20`; unknown avg `-0.1237` n `763`
- 4h: commodity avg `-0.0378` n `12`; crypto_alt avg `-1.5369` n `229`; crypto_major avg `-1.924` n `8`; equity avg `0.6004` n `91`; fx avg `0.0437` n `6`; index avg `0.0342` n `25`; metal avg `0.132` n `20`; unknown avg `0.1529` n `763`
- 24h: commodity avg `0.8149` n `12`; crypto_alt avg `-3.2277` n `229`; crypto_major avg `-2.6263` n `8`; equity avg `-1.6867` n `91`; fx avg `-0.1968` n `6`; index avg `-0.2456` n `25`; metal avg `-0.4121` n `20`; unknown avg `-0.3721` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
