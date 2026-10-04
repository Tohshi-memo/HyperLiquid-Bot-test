# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T16:07:32.070626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0177` n `13`; crypto_alt avg `-0.0393` n `235`; crypto_major avg `-0.1078` n `8`; equity avg `-0.0034` n `144`; fx avg `-0.0011` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0048` n `20`; unknown avg `-0.0741` n `1070`
- 1h: commodity avg `-0.0132` n `13`; crypto_alt avg `-0.3187` n `235`; crypto_major avg `-0.0876` n `8`; equity avg `-0.0349` n `144`; fx avg `0.0091` n `6`; index avg `-0.0115` n `26`; metal avg `-0.0172` n `20`; unknown avg `0.0719` n `1070`
- 4h: commodity avg `-0.0367` n `13`; crypto_alt avg `-0.1231` n `235`; crypto_major avg `-0.104` n `8`; equity avg `-0.0027` n `144`; fx avg `0.0081` n `6`; index avg `-0.0245` n `26`; metal avg `-0.0166` n `20`; unknown avg `-0.0376` n `1070`
- 24h: commodity avg `-0.0944` n `13`; crypto_alt avg `0.8721` n `235`; crypto_major avg `0.9213` n `8`; equity avg `0.2277` n `144`; fx avg `0.023` n `6`; index avg `-0.0053` n `26`; metal avg `-0.0174` n `20`; unknown avg `-0.1141` n `1019`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2037`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
