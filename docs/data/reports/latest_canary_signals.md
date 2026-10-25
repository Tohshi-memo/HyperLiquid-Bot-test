# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T17:07:27.147641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `13`; crypto_alt avg `0.4187` n `237`; crypto_major avg `0.3161` n `8`; equity avg `0.096` n `152`; fx avg `0.0017` n `6`; index avg `0.0205` n `26`; metal avg `0.0151` n `20`; unknown avg `0.7767` n `1200`
- 1h: commodity avg `-0.0162` n `13`; crypto_alt avg `0.4572` n `237`; crypto_major avg `0.3398` n `8`; equity avg `0.1452` n `152`; fx avg `0.0033` n `6`; index avg `0.0256` n `26`; metal avg `0.0439` n `20`; unknown avg `5.423` n `1200`
- 4h: commodity avg `-0.0708` n `13`; crypto_alt avg `1.0912` n `237`; crypto_major avg `0.7363` n `8`; equity avg `0.4785` n `152`; fx avg `-0.0051` n `6`; index avg `0.0717` n `26`; metal avg `0.0865` n `20`; unknown avg `6.9871` n `1185`
- 24h: commodity avg `-0.2173` n `13`; crypto_alt avg `1.1201` n `237`; crypto_major avg `1.6314` n `8`; equity avg `0.8858` n `152`; fx avg `0.0224` n `6`; index avg `0.1623` n `26`; metal avg `0.1786` n `20`; unknown avg `10.4847` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2257`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1704`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1695`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
