# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T20:37:53.123848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `12`; crypto_alt avg `0.1933` n `231`; crypto_major avg `0.2077` n `8`; equity avg `0.4051` n `122`; fx avg `-0.0055` n `6`; index avg `0.0268` n `25`; metal avg `0.0116` n `20`; unknown avg `0.2292` n `797`
- 1h: commodity avg `-0.0284` n `12`; crypto_alt avg `-0.3145` n `231`; crypto_major avg `-0.3443` n `8`; equity avg `0.2622` n `122`; fx avg `-0.0044` n `6`; index avg `-0.0022` n `25`; metal avg `-0.0562` n `20`; unknown avg `-0.0065` n `797`
- 4h: commodity avg `-0.3035` n `12`; crypto_alt avg `0.5337` n `231`; crypto_major avg `0.4955` n `8`; equity avg `0.8432` n `122`; fx avg `-0.0167` n `6`; index avg `0.0668` n `25`; metal avg `-0.0395` n `20`; unknown avg `0.3453` n `797`
- 24h: commodity avg `0.3545` n `12`; crypto_alt avg `-1.088` n `231`; crypto_major avg `-1.1354` n `8`; equity avg `0.103` n `122`; fx avg `-0.0668` n `6`; index avg `0.0009` n `25`; metal avg `-0.4529` n `20`; unknown avg `0.6531` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
