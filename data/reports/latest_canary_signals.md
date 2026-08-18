# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T22:22:26.250407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `0.04` n `230`; crypto_major avg `0.0225` n `8`; equity avg `0.0814` n `120`; fx avg `-0.0018` n `6`; index avg `0.0078` n `25`; metal avg `-0.0485` n `20`; unknown avg `-0.0639` n `789`
- 1h: commodity avg `0.0193` n `12`; crypto_alt avg `0.0852` n `230`; crypto_major avg `-0.0061` n `8`; equity avg `0.0537` n `120`; fx avg `-0.006` n `6`; index avg `0.0136` n `25`; metal avg `-0.0606` n `20`; unknown avg `0.7976` n `789`
- 4h: commodity avg `0.1049` n `12`; crypto_alt avg `-0.2835` n `230`; crypto_major avg `-0.1371` n `8`; equity avg `-0.1444` n `120`; fx avg `-0.0047` n `6`; index avg `-0.0281` n `25`; metal avg `-0.1591` n `20`; unknown avg `0.0383` n `789`
- 24h: commodity avg `0.2608` n `12`; crypto_alt avg `-0.6022` n `230`; crypto_major avg `0.1443` n `8`; equity avg `-4.5087` n `120`; fx avg `-0.0621` n `6`; index avg `-0.6938` n `25`; metal avg `-0.8211` n `20`; unknown avg `-0.2317` n `755`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
