# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T04:22:28.662809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `0.0882` n `234`; crypto_major avg `-0.1251` n `8`; equity avg `0.0093` n `141`; fx avg `0.015` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.4351` n `946`
- 1h: commodity avg `0.0934` n `12`; crypto_alt avg `0.4309` n `234`; crypto_major avg `-0.0296` n `8`; equity avg `-0.0668` n `141`; fx avg `-0.0115` n `6`; index avg `-0.0235` n `26`; metal avg `-0.104` n `20`; unknown avg `0.6145` n `938`
- 4h: commodity avg `-0.0682` n `12`; crypto_alt avg `-0.7315` n `234`; crypto_major avg `-0.6996` n `8`; equity avg `0.1836` n `141`; fx avg `-0.1377` n `6`; index avg `0.0564` n `26`; metal avg `-0.0617` n `20`; unknown avg `3.2249` n `938`
- 24h: commodity avg `0.4991` n `12`; crypto_alt avg `2.542` n `234`; crypto_major avg `0.9237` n `8`; equity avg `0.5768` n `141`; fx avg `-0.1426` n `6`; index avg `0.0428` n `26`; metal avg `-0.172` n `20`; unknown avg `18.5534` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
