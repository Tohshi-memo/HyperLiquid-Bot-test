# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T15:23:08.867153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0182` n `12`; crypto_alt avg `-0.121` n `234`; crypto_major avg `-0.0373` n `8`; equity avg `0.0203` n `141`; fx avg `-0.0067` n `6`; index avg `-0.0131` n `26`; metal avg `-0.0025` n `20`; unknown avg `0.7921` n `960`
- 1h: commodity avg `0.0977` n `12`; crypto_alt avg `0.4065` n `234`; crypto_major avg `0.2343` n `8`; equity avg `0.3913` n `141`; fx avg `-0.0218` n `6`; index avg `0.0683` n `26`; metal avg `0.1583` n `20`; unknown avg `8.3172` n `958`
- 4h: commodity avg `0.1221` n `12`; crypto_alt avg `-0.6286` n `234`; crypto_major avg `-0.8093` n `8`; equity avg `-0.9442` n `141`; fx avg `-0.0126` n `6`; index avg `-0.0939` n `26`; metal avg `-0.1595` n `20`; unknown avg `31.1739` n `916`
- 24h: commodity avg `-0.5768` n `12`; crypto_alt avg `2.5662` n `234`; crypto_major avg `1.5653` n `8`; equity avg `0.9006` n `141`; fx avg `-0.2585` n `6`; index avg `0.2497` n `26`; metal avg `0.2169` n `20`; unknown avg `15.6192` n `795`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
