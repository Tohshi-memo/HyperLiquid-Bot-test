# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T20:07:29.137000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0568` n `13`; crypto_alt avg `0.2007` n `235`; crypto_major avg `0.0882` n `8`; equity avg `0.1023` n `150`; fx avg `0.0076` n `6`; index avg `0.0102` n `26`; metal avg `0.0118` n `20`; unknown avg `0.6697` n `1064`
- 1h: commodity avg `0.0527` n `13`; crypto_alt avg `-0.4394` n `235`; crypto_major avg `-0.3723` n `8`; equity avg `0.0135` n `150`; fx avg `-0.0118` n `6`; index avg `-0.0186` n `26`; metal avg `-0.0616` n `20`; unknown avg `4.2234` n `1064`
- 4h: commodity avg `-0.2456` n `13`; crypto_alt avg `-0.7909` n `235`; crypto_major avg `-0.6745` n `8`; equity avg `0.2076` n `150`; fx avg `0.0065` n `6`; index avg `0.0208` n `26`; metal avg `-0.0269` n `20`; unknown avg `3.3728` n `1056`
- 24h: commodity avg `-0.0137` n `13`; crypto_alt avg `1.1901` n `235`; crypto_major avg `0.1904` n `8`; equity avg `0.9424` n `150`; fx avg `0.0125` n `6`; index avg `0.1415` n `26`; metal avg `0.5879` n `20`; unknown avg `1.6053` n `903`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
