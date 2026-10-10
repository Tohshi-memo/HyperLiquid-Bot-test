# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T01:22:32.584711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `13`; crypto_alt avg `0.0308` n `235`; crypto_major avg `0.0636` n `8`; equity avg `-0.0124` n `150`; fx avg `-0.0002` n `6`; index avg `0.0029` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.1899` n `1116`
- 1h: commodity avg `-0.023` n `13`; crypto_alt avg `-0.1066` n `235`; crypto_major avg `0.0295` n `8`; equity avg `0.0215` n `150`; fx avg `0.0034` n `6`; index avg `0.0165` n `26`; metal avg `0.0082` n `20`; unknown avg `0.0944` n `1114`
- 4h: commodity avg `0.014` n `13`; crypto_alt avg `1.0117` n `235`; crypto_major avg `0.3017` n `8`; equity avg `0.067` n `150`; fx avg `0.0021` n `6`; index avg `0.0235` n `26`; metal avg `0.0101` n `20`; unknown avg `0.0855` n `1100`
- 24h: commodity avg `-0.1388` n `13`; crypto_alt avg `2.65` n `235`; crypto_major avg `0.8117` n `8`; equity avg `0.8933` n `150`; fx avg `-0.0152` n `6`; index avg `0.1505` n `26`; metal avg `0.2852` n `20`; unknown avg `13.2634` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
