# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T20:07:30.738018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `13`; crypto_alt avg `0.1059` n `235`; crypto_major avg `0.025` n `8`; equity avg `0.0014` n `150`; fx avg `0.0` n `6`; index avg `0.0066` n `26`; metal avg `-0.0018` n `20`; unknown avg `5.158` n `1101`
- 1h: commodity avg `-0.0039` n `13`; crypto_alt avg `0.2012` n `235`; crypto_major avg `0.1263` n `8`; equity avg `0.0351` n `150`; fx avg `0.0002` n `6`; index avg `0.0096` n `26`; metal avg `-0.0083` n `20`; unknown avg `3.1558` n `1085`
- 4h: commodity avg `-0.003` n `13`; crypto_alt avg `0.3684` n `235`; crypto_major avg `-0.0085` n `8`; equity avg `0.0031` n `150`; fx avg `-0.0038` n `6`; index avg `-0.0117` n `26`; metal avg `-0.0092` n `20`; unknown avg `1.7113` n `999`
- 24h: commodity avg `-0.2062` n `13`; crypto_alt avg `3.4611` n `235`; crypto_major avg `1.4343` n `8`; equity avg `0.1972` n `150`; fx avg `-0.0046` n `6`; index avg `0.0236` n `26`; metal avg `-0.0086` n `20`; unknown avg `1.0118` n `940`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
