# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T13:22:29.647110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0284` n `12`; crypto_alt avg `0.0566` n `230`; crypto_major avg `0.245` n `8`; equity avg `0.1421` n `120`; fx avg `0.0064` n `6`; index avg `0.0182` n `25`; metal avg `0.1889` n `20`; unknown avg `0.0629` n `792`
- 1h: commodity avg `-0.0133` n `12`; crypto_alt avg `0.1894` n `230`; crypto_major avg `0.7334` n `8`; equity avg `1.2755` n `120`; fx avg `0.016` n `6`; index avg `0.1681` n `25`; metal avg `0.4992` n `20`; unknown avg `0.1108` n `792`
- 4h: commodity avg `0.0095` n `12`; crypto_alt avg `0.4626` n `230`; crypto_major avg `0.8715` n `8`; equity avg `0.8647` n `120`; fx avg `-0.0485` n `6`; index avg `0.1569` n `25`; metal avg `0.6593` n `20`; unknown avg `0.3125` n `791`
- 24h: commodity avg `0.3152` n `12`; crypto_alt avg `0.608` n `230`; crypto_major avg `1.3426` n `8`; equity avg `-0.4319` n `120`; fx avg `-0.2089` n `6`; index avg `-0.0097` n `25`; metal avg `0.2398` n `20`; unknown avg `0.0425` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
