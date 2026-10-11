# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T14:37:32.763543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `13`; crypto_alt avg `0.4585` n `235`; crypto_major avg `0.2428` n `8`; equity avg `0.0195` n `150`; fx avg `-0.0024` n `6`; index avg `0.0014` n `26`; metal avg `0.0061` n `20`; unknown avg `0.0598` n `1134`
- 1h: commodity avg `-0.1976` n `13`; crypto_alt avg `0.5139` n `235`; crypto_major avg `0.2048` n `8`; equity avg `0.0012` n `150`; fx avg `0.0054` n `6`; index avg `0.0154` n `26`; metal avg `0.0122` n `20`; unknown avg `25.0908` n `1132`
- 4h: commodity avg `-0.23` n `13`; crypto_alt avg `1.2083` n `235`; crypto_major avg `0.4944` n `8`; equity avg `0.1121` n `150`; fx avg `0.0017` n `6`; index avg `0.0075` n `26`; metal avg `0.0205` n `20`; unknown avg `1.9112` n `1053`
- 24h: commodity avg `0.0966` n `13`; crypto_alt avg `1.1569` n `235`; crypto_major avg `-0.4632` n `8`; equity avg `0.11` n `150`; fx avg `0.0061` n `6`; index avg `0.0033` n `26`; metal avg `0.0207` n `20`; unknown avg `1.1927` n `941`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
