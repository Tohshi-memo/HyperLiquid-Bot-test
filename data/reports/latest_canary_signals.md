# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T15:07:32.470818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1095` n `13`; crypto_alt avg `0.2607` n `235`; crypto_major avg `0.0989` n `8`; equity avg `0.063` n `144`; fx avg `0.033` n `6`; index avg `0.0056` n `26`; metal avg `-0.006` n `20`; unknown avg `1.2915` n `1047`
- 1h: commodity avg `0.2131` n `13`; crypto_alt avg `-0.825` n `235`; crypto_major avg `-0.8071` n `8`; equity avg `0.2458` n `144`; fx avg `0.043` n `6`; index avg `0.0606` n `26`; metal avg `0.0098` n `20`; unknown avg `1.7701` n `1007`
- 4h: commodity avg `0.0825` n `13`; crypto_alt avg `-0.7024` n `235`; crypto_major avg `-0.4541` n `8`; equity avg `0.2622` n `144`; fx avg `0.0162` n `6`; index avg `0.1229` n `26`; metal avg `-0.0831` n `20`; unknown avg `0.7757` n `989`
- 24h: commodity avg `-0.064` n `13`; crypto_alt avg `-0.0541` n `235`; crypto_major avg `0.3976` n `8`; equity avg `0.2117` n `144`; fx avg `-0.0719` n `6`; index avg `0.0574` n `26`; metal avg `0.1791` n `20`; unknown avg `-0.3859` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1982`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
