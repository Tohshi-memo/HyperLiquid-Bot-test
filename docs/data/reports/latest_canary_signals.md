# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T13:07:31.569472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0786` n `13`; crypto_alt avg `0.1987` n `237`; crypto_major avg `0.1281` n `8`; equity avg `0.0714` n `151`; fx avg `0.005` n `6`; index avg `0.0205` n `26`; metal avg `0.0152` n `20`; unknown avg `0.568` n `1175`
- 1h: commodity avg `-0.1137` n `13`; crypto_alt avg `0.3684` n `237`; crypto_major avg `0.2844` n `8`; equity avg `0.1456` n `151`; fx avg `-0.0068` n `6`; index avg `0.0467` n `26`; metal avg `-0.0739` n `20`; unknown avg `0.0724` n `1163`
- 4h: commodity avg `0.0152` n `13`; crypto_alt avg `-0.0391` n `237`; crypto_major avg `-0.0523` n `8`; equity avg `0.6486` n `151`; fx avg `0.0185` n `6`; index avg `0.049` n `26`; metal avg `-0.0565` n `20`; unknown avg `0.412` n `1151`
- 24h: commodity avg `-0.2739` n `13`; crypto_alt avg `-0.0262` n `237`; crypto_major avg `0.8611` n `8`; equity avg `3.0317` n `151`; fx avg `-0.0229` n `6`; index avg `0.4944` n `26`; metal avg `0.1505` n `20`; unknown avg `1.3685` n `951`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2028`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1566`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1327`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1156`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0607`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0589`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
