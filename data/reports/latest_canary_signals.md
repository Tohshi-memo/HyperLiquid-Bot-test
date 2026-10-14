# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T21:07:29.619635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `13`; crypto_alt avg `-0.053` n `236`; crypto_major avg `-0.1064` n `8`; equity avg `-0.0519` n `151`; fx avg `-0.0166` n `6`; index avg `-0.004` n `26`; metal avg `0.022` n `20`; unknown avg `0.3661` n `1128`
- 1h: commodity avg `-0.0121` n `13`; crypto_alt avg `-0.1497` n `236`; crypto_major avg `-0.3663` n `8`; equity avg `-0.2712` n `151`; fx avg `-0.0207` n `6`; index avg `-0.0344` n `26`; metal avg `0.0197` n `20`; unknown avg `0.254` n `1106`
- 4h: commodity avg `-0.0187` n `13`; crypto_alt avg `-0.4277` n `236`; crypto_major avg `-0.564` n `8`; equity avg `-0.8958` n `151`; fx avg `0.0042` n `6`; index avg `-0.1235` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.5588` n `1080`
- 24h: commodity avg `-0.1442` n `13`; crypto_alt avg `-2.689` n `236`; crypto_major avg `-2.3178` n `8`; equity avg `-4.4243` n `151`; fx avg `-0.1275` n `6`; index avg `-0.6136` n `26`; metal avg `-0.8463` n `20`; unknown avg `1306.6924` n `948`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0927`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0853`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0676`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0641`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0521`, n `666`, weak_sample_signal
