# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T14:52:34.493353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0486` n `12`; crypto_alt avg `0.2771` n `232`; crypto_major avg `0.2342` n `8`; equity avg `0.2322` n `134`; fx avg `0.0096` n `6`; index avg `0.0322` n `26`; metal avg `-0.0334` n `20`; unknown avg `0.2158` n `797`
- 1h: commodity avg `-0.1459` n `12`; crypto_alt avg `1.4578` n `232`; crypto_major avg `1.1496` n `8`; equity avg `0.5367` n `134`; fx avg `0.0251` n `6`; index avg `0.0095` n `26`; metal avg `-0.0039` n `20`; unknown avg `1.3779` n `781`
- 4h: commodity avg `-0.3907` n `12`; crypto_alt avg `-0.2506` n `232`; crypto_major avg `-0.1262` n `8`; equity avg `0.7563` n `134`; fx avg `0.0359` n `6`; index avg `0.0078` n `26`; metal avg `-0.0537` n `20`; unknown avg `0.5279` n `775`
- 24h: commodity avg `-0.2422` n `12`; crypto_alt avg `-0.2105` n `232`; crypto_major avg `-0.5944` n `8`; equity avg `0.5645` n `134`; fx avg `-0.072` n `6`; index avg `-0.0516` n `26`; metal avg `-0.0825` n `20`; unknown avg `7061.9452` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
