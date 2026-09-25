# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T02:52:35.297932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.3285` n `234`; crypto_major avg `-0.2724` n `8`; equity avg `-0.0606` n `141`; fx avg `0.0005` n `6`; index avg `0.0013` n `26`; metal avg `-0.0288` n `20`; unknown avg `1.4876` n `946`
- 1h: commodity avg `-0.0476` n `12`; crypto_alt avg `-0.8378` n `234`; crypto_major avg `-0.5433` n `8`; equity avg `-0.1065` n `141`; fx avg `-0.0512` n `6`; index avg `-0.0077` n `26`; metal avg `-0.056` n `20`; unknown avg `2.2146` n `944`
- 4h: commodity avg `-0.2385` n `12`; crypto_alt avg `-0.6948` n `234`; crypto_major avg `-0.2377` n `8`; equity avg `0.1828` n `141`; fx avg `-0.0948` n `6`; index avg `0.0749` n `26`; metal avg `-0.0477` n `20`; unknown avg `2.3708` n `938`
- 24h: commodity avg `0.4967` n `12`; crypto_alt avg `1.7374` n `234`; crypto_major avg `0.337` n `8`; equity avg `0.0487` n `141`; fx avg `-0.1064` n `6`; index avg `-0.0121` n `26`; metal avg `-0.1167` n `20`; unknown avg `21.8631` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
