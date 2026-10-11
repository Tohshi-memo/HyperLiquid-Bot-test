# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T14:52:25.549969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0319` n `13`; crypto_alt avg `0.1028` n `235`; crypto_major avg `0.0027` n `8`; equity avg `0.002` n `150`; fx avg `0.0064` n `6`; index avg `0.001` n `26`; metal avg `-0.006` n `20`; unknown avg `2.11` n `1134`
- 1h: commodity avg `-0.1531` n `13`; crypto_alt avg `0.6505` n `235`; crypto_major avg `0.2788` n `8`; equity avg `0.0227` n `150`; fx avg `0.0108` n `6`; index avg `0.0002` n `26`; metal avg `0.0099` n `20`; unknown avg `22.6491` n `1132`
- 4h: commodity avg `-0.2018` n `13`; crypto_alt avg `1.3223` n `235`; crypto_major avg `0.4506` n `8`; equity avg `0.122` n `150`; fx avg `0.0067` n `6`; index avg `0.0087` n `26`; metal avg `0.0182` n `20`; unknown avg `2.9774` n `1053`
- 24h: commodity avg `0.1291` n `13`; crypto_alt avg `1.1651` n `235`; crypto_major avg `-0.3338` n `8`; equity avg `0.0543` n `150`; fx avg `0.0125` n `6`; index avg `-0.0107` n `26`; metal avg `0.0101` n `20`; unknown avg `3.6057` n `941`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
