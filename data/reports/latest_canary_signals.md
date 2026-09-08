# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T23:07:30.667495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `-0.0382` n `233`; crypto_major avg `-0.0011` n `8`; equity avg `0.0346` n `134`; fx avg `-0.0088` n `6`; index avg `0.0115` n `26`; metal avg `0.0025` n `20`; unknown avg `0.5952` n `795`
- 1h: commodity avg `-0.0241` n `12`; crypto_alt avg `0.0674` n `233`; crypto_major avg `0.1244` n `8`; equity avg `0.0596` n `134`; fx avg `-0.0044` n `6`; index avg `0.0126` n `26`; metal avg `-0.0156` n `20`; unknown avg `1.0152` n `771`
- 4h: commodity avg `0.0427` n `12`; crypto_alt avg `-0.0282` n `233`; crypto_major avg `0.0403` n `8`; equity avg `-0.3207` n `134`; fx avg `-0.0213` n `6`; index avg `-0.0612` n `26`; metal avg `-0.1543` n `20`; unknown avg `-0.0407` n `725`
- 24h: commodity avg `0.0567` n `12`; crypto_alt avg `-0.017` n `232`; crypto_major avg `0.1712` n `8`; equity avg `0.578` n `134`; fx avg `-0.1051` n `6`; index avg `-0.105` n `26`; metal avg `-0.3413` n `20`; unknown avg `0.7504` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
