# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T05:22:26.560061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `0.1259` n `233`; crypto_major avg `0.0632` n `8`; equity avg `-0.1527` n `134`; fx avg `0.0051` n `6`; index avg `-0.038` n `26`; metal avg `0.0007` n `20`; unknown avg `-0.1758` n `798`
- 1h: commodity avg `-0.0237` n `12`; crypto_alt avg `0.5438` n `233`; crypto_major avg `0.3113` n `8`; equity avg `0.0404` n `134`; fx avg `0.0112` n `6`; index avg `-0.0096` n `26`; metal avg `0.076` n `20`; unknown avg `0.1352` n `790`
- 4h: commodity avg `-0.1096` n `12`; crypto_alt avg `0.81` n `233`; crypto_major avg `0.6628` n `8`; equity avg `-0.1616` n `134`; fx avg `-0.0628` n `6`; index avg `-0.0544` n `26`; metal avg `0.0603` n `20`; unknown avg `0.2334` n `785`
- 24h: commodity avg `-0.0764` n `12`; crypto_alt avg `0.0637` n `232`; crypto_major avg `1.1028` n `8`; equity avg `0.1578` n `134`; fx avg `-0.0381` n `6`; index avg `-0.1996` n `26`; metal avg `-0.3274` n `20`; unknown avg `1.159` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
