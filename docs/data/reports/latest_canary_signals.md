# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T15:52:29.503676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `13`; crypto_alt avg `0.0681` n `235`; crypto_major avg `-0.0234` n `8`; equity avg `0.0029` n `150`; fx avg `0.0` n `6`; index avg `-0.0017` n `26`; metal avg `-0.0188` n `20`; unknown avg `4.4129` n `1117`
- 1h: commodity avg `-0.0042` n `13`; crypto_alt avg `-0.0019` n `235`; crypto_major avg `-0.0521` n `8`; equity avg `0.0024` n `150`; fx avg `-0.0011` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0219` n `20`; unknown avg `1.4276` n `1107`
- 4h: commodity avg `0.0938` n `13`; crypto_alt avg `0.9434` n `235`; crypto_major avg `0.5446` n `8`; equity avg `0.1233` n `150`; fx avg `-0.0055` n `6`; index avg `0.0151` n `26`; metal avg `-0.0125` n `20`; unknown avg `1.2167` n `1101`
- 24h: commodity avg `-0.5222` n `13`; crypto_alt avg `2.5118` n `235`; crypto_major avg `0.9478` n `8`; equity avg `0.3534` n `150`; fx avg `-0.0064` n `6`; index avg `0.062` n `26`; metal avg `-0.0326` n `20`; unknown avg `1.6062` n `984`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
