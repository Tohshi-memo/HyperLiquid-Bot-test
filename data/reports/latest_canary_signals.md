# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T19:22:27.687507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0555` n `12`; crypto_alt avg `-0.0231` n `234`; crypto_major avg `0.0345` n `8`; equity avg `-0.0683` n `141`; fx avg `0.0092` n `6`; index avg `-0.0064` n `26`; metal avg `-0.0195` n `20`; unknown avg `0.5841` n `960`
- 1h: commodity avg `0.0377` n `12`; crypto_alt avg `0.1328` n `234`; crypto_major avg `-0.0783` n `8`; equity avg `-0.053` n `141`; fx avg `0.0006` n `6`; index avg `-0.0128` n `26`; metal avg `0.02` n `20`; unknown avg `0.0693` n `958`
- 4h: commodity avg `-0.1786` n `12`; crypto_alt avg `0.7792` n `234`; crypto_major avg `0.0499` n `8`; equity avg `0.1019` n `141`; fx avg `-0.0136` n `6`; index avg `0.0884` n `26`; metal avg `0.1113` n `20`; unknown avg `0.6879` n `930`
- 24h: commodity avg `-0.8878` n `12`; crypto_alt avg `1.9759` n `234`; crypto_major avg `0.4541` n `8`; equity avg `0.0757` n `141`; fx avg `-0.2626` n `6`; index avg `0.2125` n `26`; metal avg `0.1634` n `20`; unknown avg `1597.2327` n `806`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
