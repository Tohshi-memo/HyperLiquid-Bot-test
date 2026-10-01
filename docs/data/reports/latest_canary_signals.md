# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T23:22:27.193912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `13`; crypto_alt avg `0.1569` n `234`; crypto_major avg `0.1208` n `8`; equity avg `0.0102` n `142`; fx avg `-0.0039` n `6`; index avg `-0.0027` n `26`; metal avg `0.0333` n `20`; unknown avg `0.0221` n `985`
- 1h: commodity avg `-0.0572` n `13`; crypto_alt avg `0.0948` n `234`; crypto_major avg `0.052` n `8`; equity avg `0.1257` n `142`; fx avg `-0.0131` n `6`; index avg `0.0279` n `26`; metal avg `0.0567` n `20`; unknown avg `-0.0714` n `983`
- 4h: commodity avg `-0.0325` n `13`; crypto_alt avg `-0.0504` n `234`; crypto_major avg `-0.0446` n `8`; equity avg `0.1205` n `142`; fx avg `-0.0004` n `6`; index avg `0.0252` n `26`; metal avg `0.0243` n `20`; unknown avg `-0.3206` n `891`
- 24h: commodity avg `0.1038` n `13`; crypto_alt avg `-0.7365` n `234`; crypto_major avg `-0.3468` n `8`; equity avg `1.017` n `142`; fx avg `-0.1297` n `6`; index avg `0.1698` n `26`; metal avg `0.0349` n `20`; unknown avg `0.6611` n `816`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
