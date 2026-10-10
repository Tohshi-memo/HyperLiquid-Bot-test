# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T21:07:27.058089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `13`; crypto_alt avg `0.014` n `235`; crypto_major avg `-0.0214` n `8`; equity avg `0.0124` n `150`; fx avg `-0.0019` n `6`; index avg `0.0033` n `26`; metal avg `0.0047` n `20`; unknown avg `42.3783` n `1109`
- 1h: commodity avg `0.005` n `13`; crypto_alt avg `0.2665` n `235`; crypto_major avg `0.0149` n `8`; equity avg `0.02` n `150`; fx avg `-0.0016` n `6`; index avg `0.008` n `26`; metal avg `0.0095` n `20`; unknown avg `1.1003` n `1109`
- 4h: commodity avg `0.0391` n `13`; crypto_alt avg `0.6408` n `235`; crypto_major avg `0.1483` n `8`; equity avg `0.058` n `150`; fx avg `-0.0053` n `6`; index avg `0.0085` n `26`; metal avg `0.0062` n `20`; unknown avg `1.5605` n `993`
- 24h: commodity avg `-0.2736` n `13`; crypto_alt avg `3.0838` n `235`; crypto_major avg `1.0484` n `8`; equity avg `0.1597` n `150`; fx avg `-0.0065` n `6`; index avg `0.017` n `26`; metal avg `-0.0172` n `20`; unknown avg `2.5124` n `966`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
