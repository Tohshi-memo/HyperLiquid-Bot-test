# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T14:07:32.888621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.08` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.026` n `13`; crypto_alt avg `0.18` n `235`; crypto_major avg `0.1883` n `8`; equity avg `0.1114` n `144`; fx avg `-0.0108` n `6`; index avg `0.0112` n `26`; metal avg `0.0105` n `20`; unknown avg `-0.031` n `1061`
- 1h: commodity avg `-0.0188` n `13`; crypto_alt avg `0.0733` n `235`; crypto_major avg `0.4706` n `8`; equity avg `-0.0603` n `144`; fx avg `-0.0787` n `6`; index avg `0.0529` n `26`; metal avg `-0.0895` n `20`; unknown avg `36.7548` n `1061`
- 4h: commodity avg `-0.1437` n `13`; crypto_alt avg `-0.0393` n `235`; crypto_major avg `0.2662` n `8`; equity avg `-0.1009` n `144`; fx avg `-0.0513` n `6`; index avg `0.0737` n `26`; metal avg `-0.073` n `20`; unknown avg `4.7472` n `1055`
- 24h: commodity avg `-0.1456` n `13`; crypto_alt avg `1.1069` n `235`; crypto_major avg `1.3598` n `8`; equity avg `-0.0194` n `144`; fx avg `-0.1132` n `6`; index avg `-0.012` n `26`; metal avg `0.177` n `20`; unknown avg `-0.2909` n `862`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2061`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1841`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
