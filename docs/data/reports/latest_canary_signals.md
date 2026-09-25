# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T07:52:31.755145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0483` n `12`; crypto_alt avg `0.2763` n `234`; crypto_major avg `0.2151` n `8`; equity avg `0.0157` n `141`; fx avg `-0.0096` n `6`; index avg `0.0011` n `26`; metal avg `0.0082` n `20`; unknown avg `2.7788` n `946`
- 1h: commodity avg `0.1694` n `12`; crypto_alt avg `0.3606` n `234`; crypto_major avg `0.0852` n `8`; equity avg `-0.023` n `141`; fx avg `-0.0044` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0385` n `20`; unknown avg `4.3968` n `944`
- 4h: commodity avg `0.1094` n `12`; crypto_alt avg `0.7147` n `234`; crypto_major avg `0.1179` n `8`; equity avg `0.3365` n `141`; fx avg `-0.0166` n `6`; index avg `0.0727` n `26`; metal avg `0.0045` n `20`; unknown avg `2.4429` n `906`
- 24h: commodity avg `0.4303` n `12`; crypto_alt avg `1.6703` n `234`; crypto_major avg `-0.1005` n `8`; equity avg `0.8715` n `141`; fx avg `-0.1493` n `6`; index avg `0.1348` n `26`; metal avg `-0.2289` n `20`; unknown avg `13.714` n `799`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
