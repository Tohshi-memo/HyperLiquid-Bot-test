# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T04:53:08.313872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `0.3258` n `233`; crypto_major avg `0.3124` n `8`; equity avg `0.0253` n `134`; fx avg `0.0246` n `6`; index avg `0.0028` n `26`; metal avg `0.0133` n `20`; unknown avg `1.9558` n `798`
- 1h: commodity avg `-0.0468` n `12`; crypto_alt avg `1.1077` n `233`; crypto_major avg `0.9331` n `8`; equity avg `0.2089` n `134`; fx avg `-0.0045` n `6`; index avg `0.0311` n `26`; metal avg `0.0` n `20`; unknown avg `1.551` n `789`
- 4h: commodity avg `-0.1047` n `12`; crypto_alt avg `0.4394` n `233`; crypto_major avg `0.4347` n `8`; equity avg `0.1385` n `134`; fx avg `-0.0362` n `6`; index avg `0.014` n `26`; metal avg `0.0416` n `20`; unknown avg `0.9334` n `785`
- 24h: commodity avg `-0.0692` n `12`; crypto_alt avg `0.1665` n `232`; crypto_major avg `1.2455` n `8`; equity avg `0.1982` n `134`; fx avg `-0.0341` n `6`; index avg `-0.179` n `26`; metal avg `-0.4135` n `20`; unknown avg `0.0379` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
