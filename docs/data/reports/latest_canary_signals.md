# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T06:07:29.602524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `13`; crypto_alt avg `-0.1751` n `235`; crypto_major avg `-0.0964` n `8`; equity avg `-0.0318` n `150`; fx avg `0.0` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0024` n `20`; unknown avg `-0.0672` n `1098`
- 1h: commodity avg `0.015` n `13`; crypto_alt avg `0.0363` n `235`; crypto_major avg `0.1219` n `8`; equity avg `-0.0405` n `150`; fx avg `-0.0006` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0042` n `20`; unknown avg `-0.0087` n `1098`
- 4h: commodity avg `0.0567` n `13`; crypto_alt avg `0.1885` n `235`; crypto_major avg `0.0933` n `8`; equity avg `0.0152` n `150`; fx avg `0.0062` n `6`; index avg `0.0093` n `26`; metal avg `-0.0076` n `20`; unknown avg `-0.053` n `1092`
- 24h: commodity avg `0.0437` n `13`; crypto_alt avg `1.7407` n `235`; crypto_major avg `0.1662` n `8`; equity avg `-0.0478` n `150`; fx avg `-0.0316` n `6`; index avg `0.0313` n `26`; metal avg `0.0304` n `20`; unknown avg `667.6221` n `904`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
