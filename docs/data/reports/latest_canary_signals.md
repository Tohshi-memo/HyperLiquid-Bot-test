# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T07:07:30.889856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0555` n `12`; crypto_alt avg `0.1375` n `234`; crypto_major avg `-0.0005` n `8`; equity avg `0.0171` n `141`; fx avg `-0.0119` n `6`; index avg `0.0065` n `26`; metal avg `-0.0014` n `20`; unknown avg `1.3072` n `944`
- 1h: commodity avg `0.0516` n `12`; crypto_alt avg `0.0899` n `234`; crypto_major avg `-0.101` n `8`; equity avg `0.073` n `141`; fx avg `-0.0352` n `6`; index avg `0.0234` n `26`; metal avg `0.0562` n `20`; unknown avg `1.1628` n `944`
- 4h: commodity avg `0.0578` n `12`; crypto_alt avg `0.3145` n `234`; crypto_major avg `-0.1471` n `8`; equity avg `0.3082` n `141`; fx avg `-0.0379` n `6`; index avg `0.0738` n `26`; metal avg `-0.0472` n `20`; unknown avg `1.185` n `906`
- 24h: commodity avg `0.2755` n `12`; crypto_alt avg `1.9085` n `234`; crypto_major avg `0.4426` n `8`; equity avg `1.1128` n `141`; fx avg `-0.2046` n `6`; index avg `0.1839` n `26`; metal avg `-0.1264` n `20`; unknown avg `13.0227` n `799`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
