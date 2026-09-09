# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T13:52:35.419709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0664` n `12`; crypto_alt avg `0.0992` n `233`; crypto_major avg `0.112` n `8`; equity avg `-0.019` n `134`; fx avg `-0.0089` n `6`; index avg `0.0254` n `26`; metal avg `-0.0563` n `20`; unknown avg `-0.2525` n `783`
- 1h: commodity avg `-0.0605` n `12`; crypto_alt avg `-0.4336` n `233`; crypto_major avg `-0.4061` n `8`; equity avg `0.4421` n `134`; fx avg `0.0158` n `6`; index avg `0.0715` n `26`; metal avg `0.3602` n `20`; unknown avg `0.5806` n `781`
- 4h: commodity avg `-0.0859` n `12`; crypto_alt avg `0.071` n `233`; crypto_major avg `0.32` n `8`; equity avg `0.2839` n `134`; fx avg `0.022` n `6`; index avg `0.014` n `26`; metal avg `0.3998` n `20`; unknown avg `13.6252` n `774`
- 24h: commodity avg `0.1683` n `12`; crypto_alt avg `1.4225` n `232`; crypto_major avg `2.2114` n `8`; equity avg `0.6864` n `134`; fx avg `-0.0785` n `6`; index avg `-0.0872` n `26`; metal avg `0.371` n `20`; unknown avg `1.2806` n `689`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
