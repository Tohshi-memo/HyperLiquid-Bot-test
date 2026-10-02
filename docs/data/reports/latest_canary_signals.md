# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T06:37:29.098538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0359` n `13`; crypto_alt avg `-0.049` n `234`; crypto_major avg `-0.0481` n `8`; equity avg `0.0049` n `142`; fx avg `-0.0028` n `6`; index avg `0.0128` n `26`; metal avg `-0.0515` n `20`; unknown avg `0.0183` n `985`
- 1h: commodity avg `-0.1259` n `13`; crypto_alt avg `0.0018` n `234`; crypto_major avg `0.1811` n `8`; equity avg `0.0304` n `142`; fx avg `-0.04` n `6`; index avg `0.021` n `26`; metal avg `-0.039` n `20`; unknown avg `6.5901` n `953`
- 4h: commodity avg `-0.1735` n `13`; crypto_alt avg `1.0921` n `234`; crypto_major avg `1.3625` n `8`; equity avg `0.1309` n `142`; fx avg `-0.0928` n `6`; index avg `0.0356` n `26`; metal avg `0.2164` n `20`; unknown avg `7.7121` n `947`
- 24h: commodity avg `0.1205` n `13`; crypto_alt avg `0.0504` n `234`; crypto_major avg `0.9957` n `8`; equity avg `0.0008` n `142`; fx avg `-0.2991` n `6`; index avg `-0.0351` n `26`; metal avg `-0.0991` n `20`; unknown avg `1143.799` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
