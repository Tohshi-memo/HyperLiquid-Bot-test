# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T16:37:29.717698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.51` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0231` n `12`; crypto_alt avg `-0.1225` n `234`; crypto_major avg `-0.0834` n `8`; equity avg `-0.014` n `137`; fx avg `-0.0059` n `6`; index avg `-0.0069` n `27`; metal avg `-0.0091` n `20`; unknown avg `0.3836` n `911`
- 1h: commodity avg `0.0053` n `12`; crypto_alt avg `-0.0404` n `234`; crypto_major avg `0.0341` n `8`; equity avg `-0.1895` n `137`; fx avg `0.0095` n `6`; index avg `-0.0189` n `27`; metal avg `-0.033` n `20`; unknown avg `6.2041` n `909`
- 4h: commodity avg `-0.3815` n `12`; crypto_alt avg `-0.8769` n `234`; crypto_major avg `-0.3798` n `8`; equity avg `0.2301` n `137`; fx avg `-0.0003` n `6`; index avg `0.0265` n `27`; metal avg `0.0218` n `20`; unknown avg `16.5554` n `897`
- 24h: commodity avg `-0.5117` n `12`; crypto_alt avg `-2.9082` n `234`; crypto_major avg `-1.8832` n `8`; equity avg `0.9975` n `137`; fx avg `0.0466` n `6`; index avg `0.2449` n `27`; metal avg `0.3484` n `20`; unknown avg `11.6077` n `814`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
