# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T02:37:28.558687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0065` n `13`; crypto_alt avg `0.0228` n `235`; crypto_major avg `-0.0747` n `8`; equity avg `-0.0207` n `144`; fx avg `-0.0034` n `6`; index avg `-0.0145` n `26`; metal avg `-0.0174` n `20`; unknown avg `0.0472` n `1078`
- 1h: commodity avg `-0.0132` n `13`; crypto_alt avg `0.4669` n `235`; crypto_major avg `0.2958` n `8`; equity avg `-0.1195` n `144`; fx avg `0.0132` n `6`; index avg `-0.0371` n `26`; metal avg `-0.0138` n `20`; unknown avg `-0.2507` n `1072`
- 4h: commodity avg `-0.157` n `13`; crypto_alt avg `0.6623` n `235`; crypto_major avg `0.1912` n `8`; equity avg `0.2417` n `144`; fx avg `-0.0719` n `6`; index avg `0.0052` n `26`; metal avg `0.0908` n `20`; unknown avg `1.4719` n `1038`
- 24h: commodity avg `-0.362` n `13`; crypto_alt avg `1.5904` n `235`; crypto_major avg `1.856` n `8`; equity avg `0.5598` n `144`; fx avg `-0.0566` n `6`; index avg `0.0246` n `26`; metal avg `0.1745` n `20`; unknown avg `0.76` n `950`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1975`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
