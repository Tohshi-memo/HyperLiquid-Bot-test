# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T02:22:25.962719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0429` n `13`; crypto_alt avg `0.2414` n `239`; crypto_major avg `0.1202` n `8`; equity avg `0.1785` n `168`; fx avg `-0.0238` n `6`; index avg `0.0118` n `27`; metal avg `-0.097` n `20`; unknown avg `-0.1106` n `1261`
- 1h: commodity avg `0.0791` n `13`; crypto_alt avg `0.811` n `239`; crypto_major avg `0.9492` n `8`; equity avg `0.9206` n `168`; fx avg `0.0163` n `6`; index avg `0.0765` n `27`; metal avg `0.5793` n `20`; unknown avg `1.2227` n `1257`
- 4h: commodity avg `0.1981` n `13`; crypto_alt avg `0.8757` n `239`; crypto_major avg `1.1791` n `8`; equity avg `1.4409` n `168`; fx avg `-0.0255` n `6`; index avg `0.1577` n `27`; metal avg `0.6674` n `20`; unknown avg `2.304` n `1219`
- 24h: commodity avg `0.2582` n `13`; crypto_alt avg `0.9285` n `239`; crypto_major avg `0.8085` n `8`; equity avg `1.1394` n `168`; fx avg `0.0234` n `6`; index avg `0.1211` n `27`; metal avg `0.5125` n `20`; unknown avg `181.5331` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
