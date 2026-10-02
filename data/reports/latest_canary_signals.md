# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T11:37:26.566067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0144` n `13`; crypto_alt avg `0.0477` n `234`; crypto_major avg `0.0283` n `8`; equity avg `0.0094` n `142`; fx avg `-0.0165` n `6`; index avg `-0.0044` n `26`; metal avg `-0.0181` n `20`; unknown avg `-0.0902` n `985`
- 1h: commodity avg `-0.0064` n `13`; crypto_alt avg `0.0032` n `234`; crypto_major avg `0.0668` n `8`; equity avg `-0.1177` n `142`; fx avg `-0.0003` n `6`; index avg `0.0088` n `26`; metal avg `0.0327` n `20`; unknown avg `-0.4214` n `983`
- 4h: commodity avg `-0.4308` n `13`; crypto_alt avg `0.6809` n `234`; crypto_major avg `0.8787` n `8`; equity avg `0.2309` n `142`; fx avg `-0.0319` n `6`; index avg `0.084` n `26`; metal avg `-0.0299` n `20`; unknown avg `-0.5428` n `907`
- 24h: commodity avg `-0.6417` n `13`; crypto_alt avg `1.8642` n `234`; crypto_major avg `2.0795` n `8`; equity avg `0.9614` n `142`; fx avg `-0.3276` n `6`; index avg `0.2125` n `26`; metal avg `0.0607` n `20`; unknown avg `0.1029` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
