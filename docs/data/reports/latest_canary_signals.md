# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T13:52:31.559225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.46` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.2709` n `13`; crypto_alt avg `-0.3505` n `235`; crypto_major avg `-0.6087` n `8`; equity avg `-0.0336` n `143`; fx avg `0.0445` n `6`; index avg `0.0105` n `26`; metal avg `-0.0266` n `20`; unknown avg `0.9704` n `980`
- 1h: commodity avg `0.1491` n `13`; crypto_alt avg `0.1952` n `235`; crypto_major avg `-0.1493` n `8`; equity avg `0.0907` n `143`; fx avg `0.0649` n `6`; index avg `0.0334` n `26`; metal avg `-0.078` n `20`; unknown avg `27.6979` n `978`
- 4h: commodity avg `0.3166` n `13`; crypto_alt avg `0.6965` n `235`; crypto_major avg `0.1641` n `8`; equity avg `0.326` n `142`; fx avg `0.0323` n `6`; index avg `0.1678` n `26`; metal avg `0.0255` n `20`; unknown avg `9.7615` n `970`
- 24h: commodity avg `-0.4097` n `13`; crypto_alt avg `3.0531` n `235`; crypto_major avg `2.1931` n `8`; equity avg `2.1307` n `142`; fx avg `-0.2741` n `6`; index avg `0.4665` n `26`; metal avg `0.1164` n `20`; unknown avg `0.6653` n `790`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
