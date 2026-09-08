# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T16:37:35.614792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0078` n `12`; crypto_alt avg `0.2466` n `233`; crypto_major avg `0.3279` n `8`; equity avg `0.0259` n `134`; fx avg `-0.0105` n `6`; index avg `-0.0116` n `26`; metal avg `0.014` n `20`; unknown avg `0.0318` n `791`
- 1h: commodity avg `-0.0963` n `12`; crypto_alt avg `0.1502` n `232`; crypto_major avg `0.5112` n `8`; equity avg `-0.0497` n `134`; fx avg `0.0044` n `6`; index avg `-0.0233` n `26`; metal avg `-0.0547` n `20`; unknown avg `-0.0818` n `789`
- 4h: commodity avg `-0.4344` n `12`; crypto_alt avg `0.7642` n `232`; crypto_major avg `1.0422` n `8`; equity avg `0.8201` n `134`; fx avg `0.0174` n `6`; index avg `-0.0072` n `26`; metal avg `-0.0687` n `20`; unknown avg `-0.1781` n `775`
- 24h: commodity avg `-0.2875` n `12`; crypto_alt avg `1.0329` n `232`; crypto_major avg `0.6575` n `8`; equity avg `1.0176` n `134`; fx avg `-0.0678` n `6`; index avg `-0.0473` n `26`; metal avg `-0.0802` n `20`; unknown avg `7062.1471` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
