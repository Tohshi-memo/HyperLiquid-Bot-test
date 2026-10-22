# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T18:22:33.082027+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.28` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1147` n `13`; crypto_alt avg `0.1213` n `237`; crypto_major avg `0.1367` n `8`; equity avg `0.2535` n `151`; fx avg `0.0043` n `6`; index avg `0.0564` n `26`; metal avg `0.0303` n `20`; unknown avg `8.8958` n `1233`
- 1h: commodity avg `0.0345` n `13`; crypto_alt avg `-0.2487` n `237`; crypto_major avg `-0.1512` n `8`; equity avg `-0.1604` n `151`; fx avg `-0.0007` n `6`; index avg `-0.0032` n `26`; metal avg `-0.0329` n `20`; unknown avg `13.1053` n `1231`
- 4h: commodity avg `0.0404` n `13`; crypto_alt avg `-1.198` n `237`; crypto_major avg `-0.9913` n `8`; equity avg `-2.1712` n `151`; fx avg `0.0689` n `6`; index avg `-0.1465` n `26`; metal avg `-0.0993` n `20`; unknown avg `-0.227` n `1117`
- 24h: commodity avg `0.5206` n `13`; crypto_alt avg `-5.1433` n `237`; crypto_major avg `-4.0646` n `8`; equity avg `-5.192` n `151`; fx avg `-0.1254` n `6`; index avg `-0.61` n `26`; metal avg `-0.9421` n `20`; unknown avg `2.7006` n `908`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.179`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
