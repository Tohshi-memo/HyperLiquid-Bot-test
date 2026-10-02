# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T11:52:26.742909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0475` n `13`; crypto_alt avg `-0.0382` n `234`; crypto_major avg `-0.0785` n `8`; equity avg `-0.1694` n `142`; fx avg `-0.0281` n `6`; index avg `-0.0263` n `26`; metal avg `-0.0061` n `20`; unknown avg `1.5916` n `985`
- 1h: commodity avg `-0.0555` n `13`; crypto_alt avg `0.0123` n `234`; crypto_major avg `0.1124` n `8`; equity avg `-0.2457` n `142`; fx avg `-0.0442` n `6`; index avg `-0.016` n `26`; metal avg `-0.039` n `20`; unknown avg `-0.1227` n `983`
- 4h: commodity avg `-0.3197` n `13`; crypto_alt avg `0.2773` n `234`; crypto_major avg `0.6377` n `8`; equity avg `-0.0572` n `142`; fx avg `-0.0612` n `6`; index avg `0.0352` n `26`; metal avg `-0.0604` n `20`; unknown avg `-0.5759` n `907`
- 24h: commodity avg `-0.5504` n `13`; crypto_alt avg `1.7056` n `234`; crypto_major avg `1.7995` n `8`; equity avg `0.7894` n `142`; fx avg `-0.3675` n `6`; index avg `0.148` n `26`; metal avg `-0.0438` n `20`; unknown avg `-0.1342` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
