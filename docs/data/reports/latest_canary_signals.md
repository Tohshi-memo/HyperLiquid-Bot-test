# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T00:22:33.276904+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.028` n `12`; crypto_alt avg `-0.099` n `233`; crypto_major avg `0.0478` n `8`; equity avg `-0.0082` n `134`; fx avg `0.0253` n `6`; index avg `0.0017` n `26`; metal avg `-0.0177` n `20`; unknown avg `1.3091` n `797`
- 1h: commodity avg `0.0342` n `12`; crypto_alt avg `0.3438` n `233`; crypto_major avg `0.3486` n `8`; equity avg `0.1307` n `134`; fx avg `-0.0135` n `6`; index avg `0.0483` n `26`; metal avg `-0.0109` n `20`; unknown avg `0.7482` n `795`
- 4h: commodity avg `0.0812` n `12`; crypto_alt avg `0.1133` n `233`; crypto_major avg `0.4973` n `8`; equity avg `0.1384` n `134`; fx avg `-0.0612` n `6`; index avg `0.0432` n `26`; metal avg `-0.0578` n `20`; unknown avg `0.4633` n `741`
- 24h: commodity avg `0.1396` n `12`; crypto_alt avg `-0.0308` n `232`; crypto_major avg `0.5631` n `8`; equity avg `0.3256` n `134`; fx avg `-0.0514` n `6`; index avg `-0.1345` n `26`; metal avg `-0.4706` n `20`; unknown avg `6.4983` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
