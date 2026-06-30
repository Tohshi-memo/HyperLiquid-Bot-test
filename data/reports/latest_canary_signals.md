# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T16:37:33.828321+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `-0.092` n `228`; crypto_major avg `-0.1055` n `8`; equity avg `-0.0212` n `88`; fx avg `-0.0081` n `6`; index avg `0.0026` n `23`; metal avg `-0.0229` n `20`; unknown avg `-0.0456` n `765`
- 1h: commodity avg `-0.0031` n `12`; crypto_alt avg `-0.1648` n `228`; crypto_major avg `-0.1541` n `8`; equity avg `0.3067` n `88`; fx avg `-0.0263` n `6`; index avg `0.0515` n `23`; metal avg `0.0053` n `20`; unknown avg `0.0695` n `765`
- 4h: commodity avg `-0.2064` n `12`; crypto_alt avg `0.4788` n `228`; crypto_major avg `0.0701` n `8`; equity avg `0.9594` n `88`; fx avg `0.0887` n `6`; index avg `0.2446` n `23`; metal avg `0.1455` n `20`; unknown avg `-0.1996` n `765`
- 24h: commodity avg `0.1799` n `12`; crypto_alt avg `-1.6789` n `228`; crypto_major avg `-1.0651` n `8`; equity avg `1.7392` n `88`; fx avg `0.1253` n `6`; index avg `0.3975` n `23`; metal avg `0.491` n `20`; unknown avg `7.9754` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
